from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from routes.sentenceRouter import sentence_blueprint

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(sentence_blueprint, url_prefix='/sentence')

if __name__ == '__main__':
    app.run()