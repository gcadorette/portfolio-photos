class Photo:
    id = ""
    url = ""
    thumbnail_url = ""
    insert_date = None
    def __init__(self, url, thumbnail_url):
        self.id = ""
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.insert_date = None

class Photo_Click:
    def __init__(self, photo_id):
        id = ""
        photo_id = photo_id
        timestamp = None
        