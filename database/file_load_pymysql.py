# %%
import pymysql
import os

# %%
# set variables

file_path = os.getcwd()
os.chdir('..')
data_path = os.getcwd()
os.chdir(file_path)

conn_properties = {
    'host': os.getenv('OSKR_HOST'),
    'user': os.getenv('OSKR_USER'),
    'password': os.getenv('OSKR_PASS'),
    'database': os.getenv('OSKR_DB'),
    'local_infile': True,
    'charset': 'utf8mb4'
}

mysql_conn = pymysql.connect(**conn_properties)

mysql_cursor = mysql_conn.cursor()
# %%
# queries to drop and create table

drop_sql = """DROP TABLE IF EXISTS `temp`""";
create_sql = """CREATE TABLE `temp` (
    `id` int(11) ,
    `email` varchar(255) ,
    `password` varchar(255)
    )"""

# %%
# executing the queries above
mysql_cursor.execute(drop_sql)
mysql_conn.commit()

mysql_cursor.execute(create_sql)
mysql_conn.commit()

# conn.close()
# %%
# query to load infile data

load_data = f"""LOAD DATA LOCAL INFILE  '{data_path}/data/temp-upload.csv'
INTO TABLE temp
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;"""

mysql_cursor.execute(load_data)
mysql_conn.commit()

# %%
# command to close the connection to the database

mysql_conn.close()


# %%
