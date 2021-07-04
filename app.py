from flask import Flask, redirect
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from resources.bike import Bike
from resources.index import Index
import os

app = Flask(__name__)
api = Api(app)
api.add_resource(Bike, '/bikes')
api.add_resource(Index, '/')
SWAGGER_URL = '/api/docs'
API_URL = '/static/openapi.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL
    
)

app.register_blueprint(swaggerui_blueprint)

    

if __name__ == '__main__':
  app.run()