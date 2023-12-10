from flask import Flask
from flask_pymongo import PyMongo
from app.routes import upload_file

import os

app = Flask(__name__)
app.config['MONGO_URI'] = 'your_mongo_db_uri'
mongo = PyMongo(app)

# Define the folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.register_blueprint(upload_file)

# ... Other app configurations, if any
