import config

client = MongoClient(config.DB_URL, config.DB_PORT, username=DB_USERNAME, password=DB_PASSWORD)