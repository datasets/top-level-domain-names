import os
import csv
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/root/db'
data = 'data/top-level-domain-names.csv'
datapackage = './datapackage.json'
header = ['Domain', 'Type', 'Sponsoring Organization']

def update_dataset():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table", {"class": "iana-table"})
    
    rows = [header]
    for row in table.find_all('tr'):
        row_data = [cell.text.strip() for cell in row.find_all('td') if cell.text.strip()]
        if row_data:  # Only add non-empty rows
            rows.append(row_data)

    with open(data, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def update_byte_datapackage():
    # Get data file byte size
    file_stats = os.stat(data)
    file_size = file_stats.st_size

    with open(datapackage, 'r') as file:
        data_json = json.load(file)
        data_json['resources'][0]['bytes'] = int(file_size)

    with open(datapackage, 'w') as file:
        json.dump(data_json, file, indent=2)

if __name__ == '__main__':
    update_dataset()
    update_byte_datapackage()