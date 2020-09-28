from flask import render_template, request, redirect, url_for, jsonify, json
from src import app
from src.parser import Parser
from config import GOOGLE_API_KEY


app.config.from_object('config')
parser = Parser()

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/ask_question/', methods=['POST'])
def ask_question():
    if request.method == 'POST':
        if request.is_json:
            json_question = request.get_json()
            question = json_question["user_question"]

            parser = Parser()
            if parser.check_question_mark(question):
                place_object = parser.process_question(question)

                if place_object == None:
                    return {"response": "nothing"}
                else:
                    return {
                        "response": place_object.name,
                        "latitude": place_object.latitude,
                        "longitude": place_object.longitude,
                        "description": "vide", #TODO: à remplacer par place_object.description
                        "api_url": f"https://maps.googleapis.com/maps/api/js?key={GOOGLE_API_KEY}=initMap"
                        }
            else:
                return {"response": "not a question"}

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404