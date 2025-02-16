from backend.router import app
from backend import constants
from backend.client import mongodbclient
from backend.models.photomodel import Photo

from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import os

@app.route('/admin', methods=['POST'])
def upload_file():
    files = request.files.getlist("file")
    print(files)
    if len(files) == 0 or all([x == "" for x in files]):
        return "No files selected", 400
    uploaded_files = []
    invalid_files = []
    photos_to_save = []
    for file in files:
        filename = secure_filename(file.filename)
        if filename.rsplit(".", 1)[1].upper() in constants.ALLOWED_FILES:
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_path)
            thumbnail_url = f'{os.path.join(app.config["UPLOAD_FOLDER"], constants.THUMBNAILS_DIR, filename)}.{constants.THUMBNAIL_FORMAT}'
            with Image.open(full_path) as im:
                im.thumbnail(constants.THUMBNAIL_SIZE)
                im.save(thumbnail_url)
            uploaded_files.append(filename)
            photos_to_save.append(Photo(full_path, thumbnail_url))
        else:
            invalid_files.append(filename)
    mongodbclient.insert_photos(photos_to_save)
    return {
        "invalid_files": invalid_files,
        "uploaded_files": uploaded_files
    }, 200 if len(uploaded_files) > 0 else 400
