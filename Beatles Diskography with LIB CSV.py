# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, 'rb') as csv_file_input:
        #reads data and converts each row to a dictionary
        read_data = csv.DictReader(csv_file_input)
        for each_line in read_data:
            print each_line
            for key, value in each_line.iteritems():
                print "v1: ", value,
                each_line[key] = value.replace('\xe2\x80\x94', '-')

                print each_line[key]

            #add each row(now a dictionary) to the list
            data.append(each_line)

    print data[0]
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    print firstline
    print d[0]

    assert d[0] == firstline
    assert d[9] == tenthline


test()

