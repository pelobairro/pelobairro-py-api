from flask import jsonify
from flask_restful import Resource, request
import pandas as pd
import json
from geopy.distance import geodesic

class Bike(Resource):
  
  def get(self):
    lat = request.args.get('lat', default = 38.746118, type = float)
    lng = request.args.get('lng', default =  -9.109845, type = float)
    max = request.args.get('max', default = 3, type = int)
    results = []
    results = self.getParkingHotspot(lat, lng, max, results)
    return jsonify(results)
  
  
  def responseData(self, name, lat, lng, distance, type):
    return {
      'name': name,
      'lat': lat,
      'lng': lng,
      'distance': distance,
      'type': type
    }

  def getParkingHotspot(self, lat, lng, max, results):
    place =(lat, lng)
    df = pd.read_csv("data/estacionamento_com_sem_hotspot.csv", sep=',', header=None)
    for index, row in df.iterrows():
      if index > 0:
        x = geodesic(place, (row[1],row[0])).km
        if x <= max:
          results.append(self.responseData(f'{row[4]} - {row[5]} - {row[6]}', row[1], row[0], x, row[7]))
    return results
  

  