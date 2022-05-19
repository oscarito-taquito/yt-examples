'''
Two important things to do when looking to use pyodbc
This assumes you have homebrew installed (https://brew.sh)
1.) brew install unixodbc
2.) brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools
'''

import pyodbc
import os
conn_properties = {
    'server': os.getenv('SQL_SERVER_HOST'),
    'user': os.getenv('SQL_SERVER_LOGIN'),
    'password': os.getenv('SQL_SERVER_PASS'),
    'db': os.getenv('SQL_SERVER_DB'),
    'driver': '{/usr/local/Cellar/msodbcsql17/17.9.1.1/lib/libmsodbcsql.17.dylib}'
}
conn = pyodbc.connect(**conn_properties)
query = "select * from Persons"
cursor = conn.cursor()
cursor.execute(query)
for r in cursor:
    print(r)


