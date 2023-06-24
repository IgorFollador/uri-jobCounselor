from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('./config/config.py')
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from routes.sentenceRouter import *
from routes.companyRouter import *

if __name__ == '__main__':
    app.run(debug=True)