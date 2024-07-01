from router import app
import os
import constants

@app.route('/photo', methods=['GET'])
def get_all_photo():
    path = os.path.join(constants.IMG_DIR, constants.THUMBNAILS_DIR)
    imgs = os.listdir(path)
    return [os.path.join(path, x) for x in imgs]

@app.route('/photo/<id>', methods=['GET'])
def get_photo(id):
    return id