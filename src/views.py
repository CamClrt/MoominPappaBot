from flask import render_template, request, redirect, url_for, jsonify, json
from src import app
from src.parser import Parser


app.config.from_object('config')
parser = Parser()

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/ask_question/', methods=['POST'])
def ask_question():
    if request.is_json:
        json_question = request.get_json()
        question = json_question["user_question"]
        place_object = parser.define_place(question)

        if place_object == None:
            return {"response": "nothing"}
        else:
            return {
                "name": place_object.name,
                "latitude": place_object.latitude,
                "longitude": place_object.longitude,
                "description": place_object.description,
                "url": place_object.url,
                }
    else:
        print("Only a JSON file is accepted")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404