from flask import render_template, request, redirect, url_for, jsonify
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
    if request.method == 'POST':
        question = ((request.json).get('user_question'))

        if parser.check_question_mark(question):
            place_list = parser.process_question(question)
            if len(place_list) == 1:
                print(place_list)
                place = place_list[0]
                return {
                    "response": place.name,
                    "latitude": place.latitude,
                    "longitude": place.longitude,
                    "address": place.address,
                    "description": place.description,
                    }
            elif len(place_list) > 1:
                return {"response": "too many places"}
            else:
                return {"response": "nothing"}
        else:
            return {"response": "not a question"}

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404