from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('./config/config.py')


db = SQLAlchemy(app)
# TODO fazer migrate
migrate = Migrate(app, db)
from routes.sentenceRouter import *

if __name__ == '__main__':
    app.run(debug=True)