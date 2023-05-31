from flask import Blueprint, jsonify
from services.sentenceService import rateSentence

sentence_blueprint = Blueprint('sentenceRouter', __name__)

@sentence_blueprint.route('/rate', methods=['POST'])
def rate(request):
    return rateSentence(request)

@sentence_blueprint.route('/hello')
def helloworld():
    return jsonify({'text':'Hello'})