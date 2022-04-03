import requests
import re

from bs4 import BeautifulSoup

def get_urls_from_website(website_url:str):
    """"
        def: connector to a website url to retrieve all urls
        param: string
        retrn: list of strings
    """
    
    url_list = []
    page = requests.get(website_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    letter_boxes = soup.find('div', {'class':'letterboxes'})
    
    for url in letter_boxes.find_all('a'): 
        url_list.append(url['href'])

    return url_list


def get_circuits_information(circuit_url:str): 
    """"
        def: connector to circuit url to retrieve all data
        param: string
        retrn: dict
    """
    circuit_info = {}
    page = requests.get(circuit_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    circuit_id = circuit_url.rsplit(sep='/', maxsplit=1)[1]
    name = soup.find('h1').text
    circuit_info['id']=circuit_id
    circuit_info['name'] = name
    info_block = soup.find('div', {'class':'blocks blocks2'})

    for index, row in enumerate(info_block.find('table').find_all('td')):          
        if index % 2 == 0: 
            label = re.sub(r"[:\n]", '', row.text)
        else: 
            data = re.sub(r"[:\n]", '', row.text)
            circuit_info[label] = data

    data_block = soup.find('div', {'class':'blocks blocks1'})

    for row in data_block.find('table').find('tbody').find_all('tr'):
        label = 'course' + str(row.find('td').text)
        url = row.find('a')['href']
        circuit_info[label] = url

    page.close()

    return circuit_info

def get_constructors_information(constructor_url:str): 
    """"
        def: connector to constructors url to retrieve all data
        param: string
        retrn: dict
    """
    constructor_info = {}
    page = requests.get(constructor_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    circuit_id = constructor_url.rsplit(sep='/', maxsplit=1)[1]
    name = soup.find('h1').text
    constructor_info['id']=circuit_id
    constructor_info['name'] = name
    info_block = soup.find('div', {'class':'blocks blocks2'})

    for index, row in enumerate(info_block.find('table').find_all('td')):          
        if index % 2 == 0: 
            label = re.sub(r"[:\n]", '', row.text)
        else: 
            data = re.sub(r"[:\n]", '', row.text)
            constructor_info[label] = data

    page.close()

    return constructor_info

def get_drivers_information(driver_url:str):
    """"
        def: connector to drivers url to retrieve all data
        param: string
        retrn: dict
    """
    driver_info = {}
    page = requests.get(driver_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    driver_id = driver_url.rsplit(sep='/', maxsplit=1)[1]
    name = soup.find('h1').text
    driver_info['id'] = driver_id
    driver_info['name'] = name
    info_block = soup.find('div', {'class':'blocks blocks2'})

    for index, row in enumerate(info_block.find('table').find_all('td')):          
        if index % 2 == 0: 
            label = re.sub(r"[:\n]", '', row.text)
        else: 
            data = re.sub(r"[:\n]", '', row.text)
            driver_info[label] = data
    
    data_block = soup.find('div', {'class':'blocks blocks2'}).find_next_sibling('div', {'class':'blocks blocks2'}).find_next_sibling('div', {'class':'blocks blocks2'}).find_next_sibling('div', {'class':'blocks blocks2'}).find_next_sibling('div', {'class':'blocks blocks2'})
    
    for row in data_block.find('table').find('tbody').find_all('tr'):
        label = 'season ' + str(row.find('td').text)
        constructor = row.select('a:nth-of-type(1)')[1].get_text(strip=True)
        driver_info[label]=constructor

    page.close()

    return driver_info