from textblob import TextBlob
from googletrans import Translator
from flask import jsonify

def percentage(part, total):
    return 100*float(part)/float(total)

def translate(sentence):
    translator = Translator()
    sentenceTranslated = translator.translate(sentence, src='pt', dest='en').text
    return sentenceTranslated

def rateSentence(sentence):
    # logic to rate sentence
    return jsonify(sentence)

def hello(request):
    return "world"