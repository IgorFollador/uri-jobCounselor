from flask import Flask
from routes.sentenceRouter import sentence_blueprint

app = Flask(__name__)

app.register_blueprint(sentence_blueprint, url_prefix='/sentence')

if __name__ == '__main__':
    app.run()