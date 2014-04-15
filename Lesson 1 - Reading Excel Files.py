__author__ = 'Dad'
#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    #print sheet_data[2][3]
    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:",
    print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    #gets lists of coast and time columns
    coast_col = sheet.col_values(1, 1)
    time_col = sheet.col_values(0, 1)

    print max(coast_col)
    #get indexes of min and max values so we can use to get time value in other column
    max_index = coast_col.index(max(coast_col))
    min_index = coast_col.index(min(coast_col))

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    exceltime_max = time_col[max_index]
    exceltime_min = time_col[min_index]
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    print xlrd.xldate_as_tuple(exceltime_max,0)

    data = {
            'maxtime': xlrd.xldate_as_tuple(exceltime_max,0),
            'maxvalue': max(coast_col),
            'mintime': xlrd.xldate_as_tuple(exceltime_min,0),
            'minvalue': min(coast_col),
            'avgcoast': sum(coast_col)/len(coast_col)
    }
    return data


def test1():
    #open_zip(datafile)
    data = parse_file(datafile)
    print 'data received: '
    print data
    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test1()