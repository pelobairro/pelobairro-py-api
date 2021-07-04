from flask import jsonify, make_response
from flask_restful import Resource, request
import pandas as pd
import os
from geopy.distance import geodesic

class Bike(Resource):
  
  def get(self):
    lat = request.args.get('lat', default = 38.746118, type = float)
    lng = request.args.get('lng', default =  -9.109845, type = float)
    max = request.args.get('max', default = 3, type = int)
    results = []
    results = self.getResults(lat, lng, max, results)
    response = make_response(jsonify(results), 200)
    response.headers["Content-Type"] = "application/json"
    return response
  
  
  def responseData(self, name, lat, lng, distance, type):
    return {
      'name': name,
      'lat': lat,
      'lng': lng,
      'distance': distance,
      'type': type
    }

  def getResults(self, lat, lng, max, results):
    place =(lat, lng)
    path = f'{os.getcwd()}/data'
    for filename in os.listdir(path):
      df = pd.read_csv(f'{path}/{filename}', sep=',')
      for index, row in df.iterrows():
        x = geodesic(place, (row['_lat_'],row['_lng_'])).km
        if x <= max:
          results.append(self.responseData(row['_name_'], row['_lat_'], row['_lng_'], x, row['_type_']))
    return results
  

  