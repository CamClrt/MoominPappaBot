from flask import render_template, request, redirect, url_for, jsonify
from src import app

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/ask_question/', methods=['POST'])
def ask_question():
    if request.method == 'POST':
        question = (request.json).get('user_question')
    return {"response": question}
    