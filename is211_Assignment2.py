#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 2 """

import csv

import logging

import urllib2

import datetime

import argparse

def main():
    """ main function docstring"""
    logging.basicConfig(file_name='error.log')
    
    def downloadData(url):
        """function docstring"""

        urlname = urllib2.urlopen(url)
        return urlname

    def processData(data):
        """ function docstring """

        with open (data, 'r') as file1:
            csvdata = csv.reader(file1)
            datastore = {}
            dateformat = '%d/%m/%Y'

            for row in csvdata:
                if row[0] == 'id':
                    continue
            else:
                try:
                    row[2] = datetime.datetime.strptime(row[2], dateformat)

                except ValueError:
                    linenum = int(row[0]) + 1
                    idname = int(row[0])
                    log = logging.getlogger('Assignment 2')
                    log.error('Error processing line #{} for ID # {}'.format(linenum, idname))

                finally:
                    datastore[int(row[0])] = [(row[1]), (row[2])]
        return datastore

    def displayPerson(id, personData):
        """displayPerson Docstring """

        try:
            output = 'Person #{id} is {name} with birthday of {date}'
            print output.format(id = idname,
                                name = personData[idname][0],
                                date = persondData[id][1])
        except KeyError:
                print 'No person found with that ID'

        url_parser = argparse.ArgumentParser()
        url_parser.add_argument('--url', help='Url of CSV file')
        args = url_parser.parse_args()
        logging.basicConfig(filename='error.log', level=logging.ERROR)

        if args.url:
            csvData = downloadData(args.url)
            personData = processData(csvData)
            msg = 'Please enter an ID #. Enter 0 or a negative # to exit: '

        while True:
            try:
                user_input = int(raw_input(msg))
            except ValueError:
                print 'Invalid Input. Please try again'
                continue
            if user_input > 0:
                displayPerson(user_input, personData)
            else:
                print 'Thank you'
                sys.exit()
        else:
            print 'Please type --help for details'


if __name__== '__main__':
    main()
                          
                          
    

