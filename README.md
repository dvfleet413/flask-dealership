# Flask Dealership

This app was built as an API to act as a go between between a client and a third party API.  This app does not persist data to a database, but rather requests data from the NHTSA Vehicle API based on incoming requests, and passes the response back to the client.

## Installation

* Fork and clone this repository
* Though not required, it is recommended to create a virtual environment for the project
* run `$ pip install -r requirements.txt`
* run `$ flask run`
* navigate to localhost:5000, or use an api testing tool such as Postman

## Endpoints

* `/vehicle/<make>/models` - GET requests to this endpoint return all of the models from the given make.  This action gets a response from https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}

* `/vehicle/<make>/models/<year>` - GET requests to this endpoint return all of the models made within the given year by the given make.  This action gets a response from https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/{make}/modelyear/{year}