from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('./configuration/config.py')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
from routes.sentenceRouter import *

if __name__ == '__main__':
    app.run(debug=True)