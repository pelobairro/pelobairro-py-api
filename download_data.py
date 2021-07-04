from resources.bike import Bike
import requests
from pathlib import Path
import pandas as pd
import json

path = "data"

def download_data_files(url, path, filename):
  result = requests.get(url)
  Path(path).mkdir(parents=True, exist_ok=True)
  filename = f'{path}/{filename}'
  file = open(filename,'wb')
  file.write(result.content)
  file.close()
  return pd.read_csv(filename)

# geodados cml
url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_1/downloads/data?format=csv&spatialRefId=4326'
parking_hotspot_df = download_data_files(url, path, 'parking_hotspot.csv')
for index, row in parking_hotspot_df.iterrows():
  parking_hotspot_df.at[index, '_lat_'] = row['Y'] 
  parking_hotspot_df.at[index, '_lng_'] = row['X'] 
  parking_hotspot_df.at[index, '_type_'] = row['TIPO_ESTACIONAMENTO']
  parking_hotspot_df.at[index, '_name_'] = f'{row["MORADA"]} - {row["MORADA_DETALHE"]} - {row["LOCALIZACAO"]}'
parking_hotspot_df.to_csv(f'{path}/parking_hotspot.csv')

url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_2/downloads/data?format=csv&spatialRefId=4326'
parking_df = download_data_files(url, path, 'parking.csv')
for index, row in parking_df.iterrows():
  parking_df.at[index, '_lat_'] = row['Y'] 
  parking_df.at[index, '_lng_'] = row['X'] 
  parking_df.at[index, '_type_'] = row['TIPO_ESTACIONAMENTO']
  parking_df.at[index, '_name_'] = f'{row["MORADA"]} - {row["MORADA_DETALHE"]} - {row["LOCALIZACAO"]}'
parking_df.to_csv(f'{path}/parking.csv')

url = 'https://opendata.arcgis.com/api/v3/datasets/202d0f1a7f234e449761af8af14436d6_1/downloads/data?format=csv&spatialRefId=4326'
water_elements_df = download_data_files(url, path, 'water_elements.csv')
for index, row in water_elements_df.iterrows():
  if row['TIPOLOGIA'] == 'Bebedouro':
    water_elements_df.at[index, '_lat_'] = row['Y'] 
    water_elements_df.at[index, '_lng_'] = row['X'] 
    water_elements_df.at[index, '_type_'] = row['TIPOLOGIA']
    water_elements_df.at[index, '_name_'] = f'{row["DESIGNACAO"]} - {row["MORADA"]}'
water_elements_df.to_csv(f'{path}/water_elements.csv')

url = 'https://opendata.arcgis.com/api/v3/datasets/d3ae336f0988464d91bc016ec75db9b1_0/downloads/data?format=csv&spatialRefId=4326'
download_data_files(url, path, 'micromobilidade.csv')
url = 'https://opendata.arcgis.com/api/v3/datasets/440b7424a6284e0b9bf11179b95bf8d1_0/downloads/data?format=csv&spatialRefId=4326'
download_data_files(url, path, 'rede_ciclavel.csv')

# dados cml
url = 'http://coiapp.cm-lisboa.pt/api/opendata/public/download/53616c7465645f5f62a975d9194dd0ee7a0d7ffb4f36b0c0b5161a94daf4ed0e.csv?format=csv'
bikes_df = download_data_files(url, path, 'bikes.csv')
for index, row in bikes_df.iterrows():
  bikes_df.at[index, '_lat_'] = json.loads(row['position'])['coordinates'][1] 
  bikes_df.at[index, '_lng_'] = json.loads(row['position'])['coordinates'][0]
  bikes_df.at[index, '_type_'] = 'GIRABIKE'
  bikes_df.at[index, '_name_'] = row['desigcomercial']
bikes_df.to_csv(f'{path}/bikes.csv')
