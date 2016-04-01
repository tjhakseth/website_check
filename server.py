"""Lookout Backend Internship - Services/Security Homework"""
import argparse
import requests
import signal
import time
from sqlalchemy.orm import sessionmaker
from model import Status, db_connect, create_status_table


def command_line_parser():
    """Creates command line string"""

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                       help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                       const=sum, default=max,
                       help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


def db_connection():
    """Connects to postgres database"""

    engine = db_connect()
    create_status_table(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)


interval = int(raw_input("Enter number of seconds: "))
url = raw_input("Enter website: ")


def url_check(url):
    """Checks to make sure the url is valid"""

    r = requests.head(url)
    if r.status_code != 200:
        url = raw_input("Error-please enter a valid website: ")
    else:
        return url

    # try:
    #     r = requests.head(url)
    #     print(r.status_code)
    #     # prints the int of the status code. Find more at httpstatusrappers.com :)
    # except requests.ConnectionError:
    #     print("failed to connect")


def download_file(url):
    """Downloads a file and chunks it for better downloading"""

    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:# filter out keep-alive new chunks
                f.write(chunk)
                #f.flush()
    return local_filename


def signal_handler(signum, frame):
    """Timeout for websites"""

    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(10)   # Ten seconds
try:
    long_function_call()
except Exception, msg:
    print "Timed out!"


def process_site(interval, url):
    """Processes the website and adds to the database"""
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


if __name__ == '__main__':
