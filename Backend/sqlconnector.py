import configparser
import pyodbc

import pandas as pd

def get_source_connection(server_name:str, db_name:str): 
    config_file = 'C:\\Users\\adeso\\Documents\\Developpement\\Projets\\F1_Data_Analysis\\Backend\\config.ini'
    config = configparser.ConfigParser()
    config.read_file(open(config_file))
    DSN = config.get('DB', 'DSN')
    DB = config.get('DB', 'DB')

    cnxn = connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server_name+'; DATABASE=' +db_name+'; Trusted_Connection=Yes')

    return cnxn

def insert_records(file_name:str, sql_query:str):
     
     data_df = pd.read_json(file_name)

     for index, row in data_df.iterrows():
         print(data_df)

