"""Lookout Backend Internship - Services/Security Homework"""
import requests
import time
from sqlalchemy.orm import sessionmaker
from model import Status, db_connect, create_status_table

engine = db_connect()
create_status_table(engine)
Session = sessionmaker()
Session.configure(bind=engine)

interval = int(raw_input("Enter number of seconds: "))
url = raw_input("Enter website: ")


def url_check(url):
    
    r = requests.head(url)
    if r.status_code > 400:
        url = raw_input("Please enter a valid website: ")


while True:
    if interval < 1:
        interval = 60

    r = requests.get(url)
    HTTP_status_code = r.status_code
    timestamp = r.headers['Date']

    print type(HTTP_status_code)

    new_record = Status(HTTP_status_code=HTTP_status_code, url=url, timestamp=timestamp)
    session = Session()
    session.add(new_record)
    session.commit()

    print HTTP_status_code
    print url
    print timestamp
    time.sleep(interval)
