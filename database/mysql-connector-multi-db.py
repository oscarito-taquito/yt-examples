"""
Using MySQL's my.cnf to support multi database connections
by setting the option_groups argument
"""
import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf',
                                   option_groups=['client2'])
    print('Connection Successful')
    conn.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('client2 creds invalid')
    else:
        print(err)
