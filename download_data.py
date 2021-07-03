import requests
from pathlib import Path
import pandas as pd



def download_csv_geodados(url, filename):
  path = "data"
  result = requests.get(url)
  Path(path).mkdir(parents=True, exist_ok=True)
  filename = f'{path}/{filename}'
  file = open(filename,'wb')
  file.write(result.content)
  file.close()

# url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_1/downloads/data?format=csv&spatialRefId=4326'
# download_csv_geodados(url, 'estacionamento_com_sem_hotspot.csv')
# url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_1/downloads/data?format=csv&spatialRefId=4326'  
url = 'https://geodados-cml.hub.arcgis.com/datasets/estacionamento-para-veloc%C3%ADpedes/explore?location=38.744511%2C-9.159595%2C12.81&showTable=true'
html = pd.read_html(url)
print(html)
