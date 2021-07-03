import requests
from pathlib import Path
import shutil

path = "data"

url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_1/downloads/data?format=csv&spatialRefId=4326'

result = requests.get(url)

Path(path).mkdir(parents=True, exist_ok=True)

filename = f'{path}/estacionamentos.csv'

file = open(filename,'wb')
file.write(result.content)
file.close()
   
