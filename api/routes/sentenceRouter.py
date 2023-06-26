from flask import request, Response
from app import app
from services.sentenceService import *
import json


@app.route('/sentimentAnalysis', methods=['POST'])
def sentiment_analysis():
    company_id = request.headers.get('company-id')
    sentence = request.json['text']
    result = perform_sentiment_analysis(company_id, sentence)
    return Response(json.dumps(result.json()), status=200, mimetype="application/json")


@app.route('/sentimentAnalysis', methods=['GET'])
def sentiment_analysis_get():
    company_id = request.headers.get('company-id')
    value_filter = request.headers.get('value-filter')
    type_filter = request.headers.get('type-filter')
    result = get_sentiment_analysis(company_id, value_filter, type_filter)
    return Response(json.dumps(result), status=200, mimetype="application/json")
