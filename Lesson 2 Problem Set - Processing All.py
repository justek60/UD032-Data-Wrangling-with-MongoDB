__author__ = 'Dad'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
# This is example of the datastructure you should return
# Each item in the list should be a dictionary containing all the relevant data
# Note - year, month, and the flight data should be integers
# You should skip the rows that contain the TOTAL data for a year
# data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#         },
#         {"courier": "..."}
# ]
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    # This is example of the datastructure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")

    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html.read())
        #get the table we want
        flightdata = soup.find("table", {'class': 'dataTDRight'})
        #get all cells in the table
        eachrow = flightdata.find_all("td")
        cellcount = 0
        rowcount = 0
        #iterate through data (5 cells per row)
        rowdata = []
        finalrowdata=[]
        for eachcell in eachrow:

            #    continue
            rowdata.append(eachcell.get_text())
            cellcount += 1
            if cellcount == 5:
                print rowdata[0]
                #skip header row and total rows
                if rowdata[0] == "Year" or rowdata[1] == "TOTAL":
                    rowdata = []
                    cellcount = 0
                    rowcount += 1
                    print 'skipping row'
                else:
                    finalrowdata.append(rowdata)
                    rowdata = []
                    cellcount = 0
                    rowcount += 1
        print finalrowdata
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
        for eachrow in finalrowdata:
            flights={}
            # t1 = str(eachrow[2])
            # print 'int: ', int(t1.replace(',', ''))
            flights['domestic'] = int(str(eachrow[2].replace(',', '')))
            flights['international'] = int(str(eachrow[3].replace(',', '')))
            print 'flights: ', flights
            info['year'] = int(str(eachrow[0]))
            info['month'] = int(str(eachrow[1]))
            info['flights'] = flights
            data.append(info)
    print 'data: ', data
    return data


def test():
    print "Running a simple test..."
    #open_zip(datadir)
    files = process_all(datadir)
    data = []
    for f in files:
        data += process_file(f)
    assert len(data) == 399
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}

    print "... success!"

if __name__ == "__main__":
    test()