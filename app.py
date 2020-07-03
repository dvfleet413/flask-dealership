from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from resources.routes import initialize_routes

load_dotenv()
app = Flask(__name__)
api = Api(app)

initialize_routes(api)