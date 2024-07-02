from flask import Flask
from . import constants

app = Flask(__name__, static_folder="./static")

app.config['UPLOAD_FOLDER'] = constants.IMG_DIR
app.config['UPLOAD_FOLDER'] = constants.FILE_SIZE_MAX_MB * 1024 * 1024
from backend.routes import admin, photo