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
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    
    # data colected by ESP8266
    dataSentences = [sentence]
    
    for sentence in dataSentences:
        polarity += sentence.sentiment.polarity
        print(sentence, "\n", sentence.sentiment, '\n')
        
        if (sentence.sentiment.polarity == 0):
            neutral += 1
        elif (sentence.sentiment.polarity < 0):
            negative += 1
        elif (sentence.sentiment.polarity > 0):
            positive += 1

    positive = format(percentage(positive, len(dataSentences)), '.2f')
    negative = format(percentage(negative, len(dataSentences)), '.2f')
    neutral = format(percentage(neutral, len(dataSentences)), '.2f')
    
    return jsonify(sentence)

def hello(request):
    return "world"