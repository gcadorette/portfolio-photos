from flask import Flask
import constants
app = Flask(__name__, static_folder="./static")
app.config['UPLOAD_FOLDER'] = constants.IMG_DIR

from routes import photo, admin