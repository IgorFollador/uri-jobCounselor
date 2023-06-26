from textblob import TextBlob
from models.sentences import Sentence
from models.companies import Company
import datetime
from sqlalchemy.sql import extract
from googletrans import Translator
from flask import jsonify
from app import db

def percentage(part, total):
    return 100*float(part)/float(total)

def translate(sentence):
    translator = Translator()
    sentenceTranslated = translator.translate(sentence, src='pt', dest='en').text
    return sentenceTranslated

def rateSentence(sentence):
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    
    periodSentences = [sentence]
    
    for sentence in periodSentences:
        polarity += sentence.sentiment.polarity
        print(sentence, "\n", sentence.sentiment, '\n')
        
        if (sentence.sentiment.polarity == 0):
            neutral += 1
        elif (sentence.sentiment.polarity < 0):
            negative += 1
        elif (sentence.sentiment.polarity > 0):
            positive += 1

    positive = format(percentage(positive, len(periodSentences)), '.2f')
    negative = format(percentage(negative, len(periodSentences)), '.2f')
    neutral = format(percentage(neutral, len(periodSentences)), '.2f')
    
    return jsonify(sentence)

def perform_sentiment_analysis(company_id, sentence):
    text = TextBlob(sentence)
    polarity = 0
    polarity += text.sentiment.polarity
    polarity = (polarity + 1) * 5
    current_date_time = datetime.datetime.now()
    analysis_result = Sentence(grade=polarity, sentence=sentence, date=current_date_time, company_id=company_id)
    db.session.add(analysis_result)
    db.session.commit()

    company = Company.query.get(company_id)
    sentence_grades_sum = sum(sentence.grade for sentence in company.sentences)
    company.grade = float(sentence_grades_sum / len(company.sentences))
    db.session.add(company)
    db.session.commit()

    return analysis_result

def get_sentiment_analysis(company_id, value_filter=None, type_filter=None):
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

    average_grade_per_day = {}

    for sentence in sentences:
        period = sentence.date.strftime('%Y-%m-%d')
        if type_filter == 'day':
            period = sentence.date.strftime('%Y-%m-%d %H')
        elif type_filter == 'year':
            period = sentence.date.strftime('%Y-%m')

        average_grade_per_day.setdefault(period, []).append(sentence.grade)

    result = []

    for period, daily_grades in average_grade_per_day.items():
        grade = {
            'grade': round(float(sum(daily_grades) / len(daily_grades)), 2),
            'date': period
        }
        result.append(grade)

    return result