import dimconnector
import configparser
import os 

from datetime import date

import pandas as pd

def pipelines(): 

    circuits_url = 'https://www.racing-statistics.com/en/circuits'
    constructors_url = 'https://www.racing-statistics.com/en/f1-constructors'
    drivers_url = 'https://www.racing-statistics.com/en/f1-drivers'

    create_db_files(drivers_url, 'drivers')


def create_db_files(website, file_name):
    config_file = 'C:\\Users\\adeso\\Documents\\Developpement\\Projets\\F1_Data_Analysis\\Backend\\config.ini'
    config = configparser.ConfigParser()
    config.read_file(open(config_file))
    db_dir = config.get('FILE', 'DB_DIR')

    url_list = dimconnector.get_urls_from_website(website)
    for count, url in enumerate(url_list):
        if file_name == 'circuits':
            info_dict = dimconnector.get_circuits_information(url)
        if file_name == 'constructors':
            info_dict = dimconnector.get_constructors_information(url)
        if file_name == 'drivers':
            info_dict = dimconnector.get_drivers_information(url)
        
        if count == 0: 
            info_df = pd.DataFrame(columns=info_dict.keys())
        info_df = info_df.append(info_dict, ignore_index=True)
    
    save_to_json(info_df, db_dir, file_name)

def save_to_json(data_df:pd.DataFrame, dir:str, file_name:str): 
    """ 
        save datframe to a json file
    """
    
    json_file = dir + '\\' + file_name + '.json'
    old_file = dir + '\\old\\' + str(date.today()) + '_' + file_name + '.json'

    try: 
        os.rename(json_file, old_file)

    except FileNotFoundError: 
        # Remove and use logs
        print('file does not exist')
    
    except FileExistsError:
        os.remove(old_file)

    finally:
        data_df.to_json(json_file, orient='index')



pipelines()