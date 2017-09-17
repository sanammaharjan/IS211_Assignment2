#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 2 """

import csv
import logging
import datetime
import urllib2
from StringIO import StringIO
import argparse
import sys

logging.basicConfig(filename='error.log', level=logging.DEBUG)
# parsing url arguments from command line
parser = argparse.ArgumentParser(description='Assignment 2 to paas csv url from command line')
parser.add_argument('--url', action="store", dest="url", type=str)
args = parser.parse_args()

def downloadData(url):
    """
    It allows user to pass url value while calling function
    :param url: link of weburl
    :return: return a data from url
    """
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


# function open csv and read
def processData(csvfile):
    """
    It process csv data and check the date format.
    :param csvfile: name of the csv file
    :return: data of csv into dictionary
    """
    reader = csv.reader(StringIO(csvfile))
    next(reader)  # skipping header row
    csvdict = {}  # creating empty dictionary
    lineno = 1  # counter for line number
    dformat = '%d/%m/%Y'
    for row in reader:
        id = row[0]
        name = row[1]
        birthday = row[2]
        if id != 'id':
            id = int(id)
        try:
            checkdate = datetime.datetime.strptime(birthday, dformat)
            lineno += 1
        except Exception, e:
            logging.error('Error processing line #{} for id #{}'.format(lineno, id))
        finally:
            csvdict[id] = [(name, birthday)]
    return csvdict

def displayPerson(id, personData):
    """
    It displays the information of the user based on Id #
    :param id: ID number
    :param personData: dictioary which contains all data of birthday, name and ID
    :return: Print ID, Name and birthday
    """
    try:
        print 'Person # {} is {} with a birth of {}'.format(id, personData[id][0][0], personData[id][0][1])
    except Exception, e:
        logging.warning('User typed wrong id')
        print 'No user found with that id'


def main():
    """
    Main function to combine all function.
    :return: Print User information
    """
    datasource = downloadData(args.url)  # parsing url value for command line
    personData = processData(datasource) # processing CSV data using URL

    if args.url:
        datasource = downloadData(args.url)
        personData = processData(datasource)

    while True:
        try:
            input = int(raw_input('Note: Enter 0 or a negative # to exit. \n Please enter and ID # : '))
        except ValueError:
            print 'Invalid Input. Please try again'
            continue
        if input > 0:
            displayPerson(input, personData)
        else:
            print 'Thank you'
            sys.exit()

if __name__ == "__main__":
    main()
