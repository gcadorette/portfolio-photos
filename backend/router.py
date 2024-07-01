from flask import Flask
from . import constants

app = Flask(__name__, static_folder="./static")

app.config['UPLOAD_FOLDER'] = constants.IMG_DIR

from backend.routes import admin, photo