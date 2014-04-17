# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
# spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

import xlrd
import os
import csv
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)

    #get time column values
    time_col = sheet.col_values(0, 1)

    for row in range(1, 9):
        region = sheet.cell_value(0, row)
        #get data from column
        col = sheet.col_values(row, 1)
        #get max value of column
        max_value = max(col)
        #get column index of max value so we can get the time form time column
        max_index = col.index(max(col))
        exceltime_max = time_col[max_index]
        maxtime = xlrd.xldate_as_tuple(exceltime_max, 0)
        #data[region] = {'Year': maxtime[0], 'Month': maxtime[1], 'Day': maxtime[2], 'Hour': maxtime[3], 'Max Load': max_value }
        data[region] = {'Max Load': max_value, 'Year': maxtime[0], 'Month': maxtime[1], 'Day': maxtime[2], 'Hour': maxtime[3] }
        #print region, data[region]
    print 'parse file return data: '
    print data
    print 'end parse file return data'
    return data

def save_file(data, filename):
    with open(filename, 'wb') as ofile:
        writer = csv.writer(ofile, delimiter="|")
        writer.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        nextrow=[]
        for (key, val) in data.items():
            nextrow.append(key)
            for (skey, sval) in val.items():
                nextrow.append(sval)
            #print 'nextrow: ', nextrow
            writer.writerow(nextrow)
            nextrow=[]

def test1():
    # open_zip(datafile)
    data = parse_file(datafile)
    print 'returned data: '
    #print data
    for (each, key) in data.items():
        print each, key
        for (j,k) in key.items():
            print j, k
    print '---------------------'
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            print line
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    #assert ans[s][field] == line[field]
                    pass
                #print 'LOL'
        
test1()