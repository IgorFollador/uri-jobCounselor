from flask import request, Response
from googletrans import Translator
from textblob import TextBlob
from app import app, db
from models.sentences import Sentence
from models.companies import Company
import datetime
import json
from sqlalchemy.sql import extract


def translate(sentence):
    translator = Translator()
    sentenceTranslated = translator.translate(sentence, src='pt', dest='en').text
    return sentenceTranslated

# TODO separar regras de negocio em arquivo service
# ~e melhorar os nomes de variaveis~
@app.route('/sentimentAnalysis', methods=['POST'])
def sentiment_analysis():
    company_id = request.headers.get('company-id')
    sentence = request.json['text']
    text = TextBlob(sentence)
    polarity = 0
    polarity += text.sentiment.polarity
    polarity = (polarity + 1) * 5
    data_hora_atual = datetime.datetime.now()
    funciona = Sentence(grade=polarity, sentence=sentence, date=data_hora_atual, company_id=company_id)
    db.session.add(funciona)
    db.session.commit()

    company = Company.query.get(company_id)
    sentence_grandes = 0
    for sentence in company.sentences:
        sentence_grandes += sentence.grade

    company.grade = float(sentence_grandes/len(company.sentences))
    db.session.add(company)
    db.session.commit()

    return Response(json.dumps(funciona.json()), status=200, mimetype="application/json")


# TODO melhorar o nome das váriaveis
@app.route('/sentimentAnalysis', methods=['GET'])
def sentiment_analysis_get():
    company_id = request.headers.get('company-id')
    value_filter = request.headers.get('value-filter')
    type_filter = request.headers.get('type-filter')
    if value_filter and type_filter:
        sentences = Sentence.query.filter(Sentence.company_id == company_id,
                                          extract(type_filter, Sentence.date) == value_filter)\
            .order_by(Sentence.date).all()
    elif value_filter and not type_filter:
        sentences = Sentence.query.filter(Sentence.company_id == company_id,
                                          extract('month', Sentence.date) == value_filter)\
            .order_by(Sentence.date).all()
    else:
        sentences = Sentence.query.filter(Sentence.company_id == company_id).order_by(Sentence.date).all()

    media_notas_por_dia = {}

    for sentence in sentences:
        data = sentence.date.strftime('%Y-%m-%d')
        if type_filter == 'day':
            data = sentence.date.strftime('%Y-%m-%d %H')
        elif type_filter == 'year':
            data = sentence.date.strftime('%Y-%m')
            print(data)

        media_notas_por_dia[data] = media_notas_por_dia.get(data, [])
        media_notas_por_dia[data].append(sentence.grade)

    result = []

    for data, notas_dia in media_notas_por_dia.items():
        grade = {
            'grade': round(float(sum(notas_dia) / len(notas_dia)), 2),
            'date': data
        }
        result.append(grade)

    return Response(json.dumps(result), status=200, mimetype="application/json")
