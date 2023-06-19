from flask import jsonify, request, Response
from api import app, db
from models.sentences import Sentence
import datetime
import json


@app.route('/sentimentAnalysis', methods=['POST'])
def sentiment_analysis():
    sentence = request.json['text']
    data_hora_atual = datetime.datetime.now()
    funciona = Sentence(grade=7, sentence=sentence, date=data_hora_atual)
    db.session.add(funciona)
    db.session.commit()

    return jsonify()


@app.route('/sentimentAnalysis', methods=['GET'])
def sentiment_analysis_get():
    sentences = Sentence.query.all()
    sentences_json = [sentence.json() for sentence in sentences]

    return Response(json.dumps(sentences_json), status=200, mimetype="application/json")
