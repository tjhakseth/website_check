"""sitecheck will check a site every 60 seconds or a specified interval,
 and stores the status code in a SQL database"""
import argparse
import requests
import time
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from model import Status, db_connect, create_status_table


def command_line_parser():
    """Parses command line string"""

    parser = argparse.ArgumentParser(description="""Contacts a specific website
        at a specified interval to determine if the website is available""")
    parser.add_argument('-u', '--url', metavar='URL', type=str,
                       help='URL to check', required=True, dest='url')
    parser.add_argument('-d', '--database', metavar='DATABASE', type=str,
                       help='Database connection string', required=True, 
                       dest='database')
    parser.add_argument('-i', '--interval', metavar='INTERVAL', type=int,
                       help='interval', default=60, dest='interval')

    args = parser.parse_args()
    return args


def db_connection(database):
    """Connects to the database"""

    engine = db_connect(database)
    create_status_table(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)

    return Session


def url_check(url):
    """Checks to make sure the website exists"""

    try:
        r = requests.head(url, timeout=10)
        return(r.status_code)

    except requests.ConnectionError:
        print("failed to connect")
        return None


def process_site(interval, url, Session):
    """Processes the website and adds to the database"""

    while True:
        HTTP_status_code = url_check(url)
        timestamp = datetime.now()

        new_record = Status(HTTP_status_code=HTTP_status_code, 
                            url=url, 
                            timestamp=timestamp)
        session = Session()
        session.add(new_record)
        session.commit()

        print HTTP_status_code
        print url
        print timestamp
        time.sleep(interval)


if __name__ == '__main__':
    options = command_line_parser()
    Session = db_connection(options.database)
    process_site(options.interval, options.url, Session)
