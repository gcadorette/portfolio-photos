from router import app
from flask import Flask, flash, request, redirect, url_for
from werkzeug import secure_filename
import os
import constants
import Image

def filter_valid_files(files):
    return [x for x in files if "." in x and x.rsplit(".", 1)[1].upper() in constants.ALLOWED_FILES]

@app.route('/admin', methods=['POST'])
def upload_file():
    files = request.files.getlist("file")
    print(files)
    if len(files) == 0 or all([x == "" for x in files]):
        return "No files selected", 400
    uploaded_files = []
    invalid_files = []
    for file in files:
        filename = secure_filename(file.filename)
        if filename.rsplit(".", 1)[1].upper() in constants.ALLOWED_FILES:
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_path)
            
            with Image.open(full_path) as im:
                im.thumbnail(constants.THUMBNAIL_SIZE)
                im.save(os.path.join(app.config['UPLOAD_FOLDER'], constants.THUMBNAILS_DIR, filename), "JPEG")
            uploaded_files.append(filename)
        else:
            invalid_files.append(filename)
    return {
        "invalid_files": invalid_files,
        "uploaded_files": uploaded_files
    }, 200 if len(uploaded_files) > 0 else 400
