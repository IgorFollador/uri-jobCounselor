from flask import request, Response
from googletrans import Translator
from textblob import TextBlob
from api import app, db
from models.sentences import Sentence
import datetime
import json
from sqlalchemy.sql import extract


def translate(sentence):
    translator = Translator()
    sentenceTranslated = translator.translate(sentence, src='pt', dest='en').text
    return sentenceTranslated

# TODO traduzir sentença para inglês
# TODO separar regras de negocio em arquivo service
# ~e melhorar os nomes de variaveis~
@app.route('/sentimentAnalysis', methods=['POST'])
def sentiment_analysis():
    sentence = request.json['text']
    # text = TextBlob(translate(sentence))
    text = TextBlob(sentence)
    polarity = 0
    polarity += text.sentiment.polarity
    polarity = (polarity + 1) * 5
    data_hora_atual = datetime.datetime.now()
    funciona = Sentence(grade=polarity, sentence=sentence, date=data_hora_atual)
    db.session.add(funciona)
    db.session.commit()

    return Response(json.dumps(funciona.json()), status=200, mimetype="application/json")


# TODO melhorar o nome das váriaveis
@app.route('/sentimentAnalysis', methods=['GET'])
def sentiment_analysis_get():
    value_filter = request.headers.get('value-filter')
    type_filter = request.headers.get('type-filter')
    if value_filter and type_filter:
        sentences = Sentence.query.filter(extract(type_filter, Sentence.date) == value_filter).all()
    elif value_filter and not type_filter:
        sentences = Sentence.query.filter(extract('month', Sentence.date) == value_filter).all()
    else:
        sentences = Sentence.query.all()

    sentences_json = [sentence.json() for sentence in sentences]

    return Response(json.dumps(sentences_json), status=200, mimetype="application/json")
