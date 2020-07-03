from flask import Response, request
from flask_restful import Resource
import requests

from IPython import embed

class CarsApi(Resource):
    def get(self, make):
        key = {"format": "json"}
        r = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}', params=key)
        response = r.text
        return Response(response, 200)

class CarApi(Resource):
    def get(self, make, year):
        key = {"format": "json"}
        r = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/{make}/modelyear/{year}', params=key)
        response = r.text
        return Response(response, 200)