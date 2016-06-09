# website_chcek will check a site every 60 seconds or a specified interval,
 and stores the status code in a SQL database"""

## Install requirements.txt

`$ pip install -r requirements.txt`

## Steps to create Database:
 
 Download/Run postgres
 
 `$ dropdb exampledb`
 
 `$ createdb exampledb`
 
## To run the program
Command Line Syntax:

`$ python sitecheck.py -u <url> -d <database connection string> [-i interval]`

Example:

`$ python sitecheck.py -u http://www.google.com -d postgresql://localhost/exampledb -i 2`

For full help:

`$ python sitecheck.py --help`
