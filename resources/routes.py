from .car import CarsApi, CarApi

def initialize_routes(api):
    api.add_resource(CarsApi, '/vehicle/<make>/models')
    api.add_resource(CarApi, '/vehicle/<make>/models/<year>')