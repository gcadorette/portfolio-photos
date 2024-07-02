from backend.router import app
import os
import backend.constants
from backend.models.photomodel import Photo_Click
from backend.client import mongodbclient

@app.route('/photo', methods=['GET'])
def get_all_photo_thumbnails():
    all_photos = mongodbclient.get_all_photos()
    all_photos.sort(key=lambda x: x.insert_date, reverse=True)
    return [photo.thumbnail_url for photo in all_photos]

@app.route('/photo/<id>', methods=['GET'])
def get_photo(id):
    if id:
        mongodbclient.insert_click(Photo_Click(id))
        photo = mongodbclient.get_photo()
        return photo.url, 200
    return "no id sent", 400
    