import requests
from pathlib import Path
import pandas as pd

def download_geodados(url, filename):
  path = "data"
  result = requests.get(url)
  Path(path).mkdir(parents=True, exist_ok=True)
  filename = f'{path}/{filename}'
  file = open(filename,'wb')
  file.write(result.content)
  file.close()

url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_1/downloads/data?format=csv&spatialRefId=4326'
download_geodados(url, 'estacionamento_com_sem_hotspot.csv')
url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_2/downloads/data?format=csv&spatialRefId=4326'
download_geodados(url, 'estacionamentos.csv')  
url = 'https://opendata.arcgis.com/api/v3/datasets/d3ae336f0988464d91bc016ec75db9b1_0/downloads/data?format=csv&spatialRefId=4326'
download_geodados(url, 'micromobilidade.csv')