import pyodbc
conn_properties = {
    'server': 'oskrvpydb.mssql.somee.com',
    'user': 'oscarvalles_SQLLogin_1',
    'password': 'qg4umuntt6',
    'db': 'oskrvpydb',
    'driver': '{/usr/local/Cellar/msodbcsql17/17.9.1.1/lib/libmsodbcsql.17.dylib}'
}
conn = pyodbc.connect(**conn_properties)
query = "select * from Persons"
cursor = conn.cursor()
cursor.execute(query)
for r in cursor:
    print(r)
