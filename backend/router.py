from flask import Flask
import constants



app = Flask(__name__, static_folder="./static")

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

app.config['UPLOAD_FOLDER'] = constants.IMG_DIR
app.config['DEBUG'] = True
app.config['MONGO_URI'] = config['PROD']['DB_URI']

from routes import photo, admin