from sqlalchemy import create_engine
username = 'root'
password = 'password'
host = 'localhost'
dbname = 'test_sqlAlchemy'
port = '3306'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}')

import pymysql

connection = engine.connect()
if connection:
    print('Connection established to MySQL with PyMySQL')
else:
    print('Connection established to MySQL')
connection.close()