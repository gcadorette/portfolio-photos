from pymongo import MongoClient
import datetime
from backend.models.photomodel import Photo, Photo_Click
from backend.helper import date_helper, configloader

client = MongoClient(configloader.getenv("CONNECTION_STRING"))

db = client.portfolio

photos_collection = db.photos
photo_clicks_collection = db.photo_clicks

def get_all_photos():
    photos_from_db = photos_collection.find()
    photos = []
    for photo_from_db in photos_from_db:
        photos.append(_photo_from_db_to_photo(photo_from_db))

    photos_from_db.sort(key=lambda x: x.insert_date, reverse=True)
    return photos

def get_photo(id):
    photo_from_db = photos_collection.find_one({"_id": id})
    photo = _photo_from_db_to_photo(photo_from_db)
    return photo

def insert_photos(photos):
    photos_db = []
    for photo in photos:
        photos_db.append(_photo_to_photo_from_db(photo))
    photos_collection.insert_many(photos_db)

def get_clicks_for_photo(photo_id):
    pcs_db = photo_clicks_collection.find({"photo_id": photo_id})
    photo_clicks = []
    for pc_db in pcs_db:
        photo_clicks.append(_pc_db_to_photo_click(pc))
    return photo_clicks

def insert_click(photo_click):
    photo_clicks_collection.insert_one(_photo_click_to_pc_db(photo_click))



def _photo_from_db_to_photo(photo_from_db):
    photo = Photo()
    photo.id = photo_from_db["_id"]
    photo.url = photo_from_db["url"]
    photo.thumbnail_url = photo_from_db["thumbnail_url"]
    photo.insert_date = date_helper.to_datetime(photo_from_db["insert_date"])
    return photo

def _pc_db_to_photo_click(pc_db):
    photo_click = Photo_Click()
    photo_click.id = pc_db["_id"]
    photo_click.photo_id = pc_db["photo_id"]
    photo_click.timestamp = date_helper.to_datetime(pc_db["timestamp"])

def _photo_to_photo_from_db(photo):
    return {
        "url": photo.url,
        "thumbnail_url": photo.thumbnail_url,
        "insert_date": date_helper.timestamp_now()
    }

def _photo_click_to_pc_db(photo_click):
    return {
        "photo_id": photo_click.photo_id,
        "timestamp": date_helper.timestamp_now()
    }