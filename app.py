from flask import Flask, jsonify, request, send_file
from flask_restful import Resource, Api
from pathlib import Path
import io

# Create Flask App
app = Flask(__name__)
# Create API Object
api = Api(app)


class Hello(Resource):

    def get(self):
        return {"Message": "Hello World"}




# Add Defined Resource & Corresponding Urls
api.add_resource(Hello, "/")

if __name__ == "__main__":
    app.run()