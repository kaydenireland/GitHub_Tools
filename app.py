from flask import Flask, jsonify, request, send_file
from flask_restful import Resource, Api
from trending_repos import scraper
from pathlib import Path
import io

# Create Flask App
app = Flask(__name__)
# Create API Object
api = Api(app)


class Hello(Resource):

    def get(self):
        return {"Message": "Hello World"}

class Trending(Resource):

    def get(self):
        lang = request.args.get("lang", "").strip().lower()

        repos = scraper.get_repos(lang)
        return jsonify([repo.to_dict() for repo in repos])



# Add Defined Resource & Corresponding Urls
api.add_resource(Hello, "/")
api.add_resource(Trending, "/trending/")

