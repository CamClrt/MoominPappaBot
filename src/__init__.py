"""This module initialize the application"""

from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from src import views  # noqa: E402 F401
