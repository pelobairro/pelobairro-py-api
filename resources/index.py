from flask import redirect
from flask_restful import Resource

class Index(Resource):
  
  def get(self):
      print('entrou aqui')
      return redirect("/api/docs", code=302)