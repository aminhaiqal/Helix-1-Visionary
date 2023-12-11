from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

app.config.from_object('app.config.Config')

from . import routes