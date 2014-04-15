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
    with open(datafile, "rb") as f:
        fields = f.readline()
        fields = fields.rstrip('\n')
        fields = fields.split(',')

        count = 0

        for nextline in f:
            if count == 10:
                break
            nextline = nextline.rstrip('\n') # strip line returns
            linelist = nextline.split(',')#create a list from every field

            for i in range(len(linelist)):
                linelist[i] = linelist[i].replace('\xe2\x80\x94', '-')
                linelist[i] = linelist[i].strip()

            entry = {}
            for i, value in enumerate(linelist):
                #print fields[i]
                entry[fields[i]] = value

            data.append(entry)
            count += 1

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    assert d[0] == firstline
    assert d[9] == tenthline


test()

