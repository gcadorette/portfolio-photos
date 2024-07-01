import datetime

FORMAT = '%Y-%m-%d %H:%M:%S'

def timestamp_now():
    return datetime.now().strftime('FORMAT')

def to_datetime(date_str):
    return datetime.strptime(date_str, FORMAT)