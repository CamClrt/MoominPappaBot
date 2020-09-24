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
        question = ((request.json).get('user_question')).capitalize()

        if parser.check_question_mark(question):
            #TODO: parser la question & recevoir la substance
            #TODO: contacter l'API Google Map & former la réponse
            #TODO: contacter l'API Google Map & former la réponse
            #TODO: formater la réponse & la renvoyer
            return {"response": question}
        else:
            return {"response": "not a question"}

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404