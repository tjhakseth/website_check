# Lookout Backend Internship - Services/Security Homework

## Install requirements.txt

`$ pip install -r requirements.txt`

## Steps to create Database:
 
 Download/Run postgres
 
 `$ dropdb lookoutdb`
 
 `$ createdb lookoutdb`
 
## To run the program
Command Line Syntax:

`$ python sitecheck.py -u <url> -d <database connection string> [-i interval]`

Example:

`$ python sitecheck.py -u http://www.google.com -d postgresql://localhost/lookoutdb -i 2`

For full help:

`$ python sitecheck.py --help`
