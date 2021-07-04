from flask import Flask, Blueprint
from flask_restful import Api
from resources.bike import Bike

app = Flask(__name__)
api = Api(app)
api.add_resource(Bike, '/bikes')

if __name__ == '__main__':
  app.run()