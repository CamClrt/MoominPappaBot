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
        parser = Parser()
        if parser.check_question_mark(question):
            placeObject = parser.process_question(question)
            print(placeObject)
            if placeObject == None:
                return {"response": "nothing"}
            else:
                return {
                    "response": placeObject.name,
                    "latitude": placeObject.latitude,
                    "longitude": placeObject.longitude,
                    "address": placeObject.address,
                    "description": placeObject.description,
                    }
        else:
            return {"response": "not a question"}

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404