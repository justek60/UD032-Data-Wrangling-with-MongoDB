__author__ = 'Dad'
"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year (column AH - column 34?)
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def get_number(number):
    #return an integer if valid string, none is not valid
    try:
        # This will return the equivalent of calling 'int' directly, but it
        # will also allow for floats.
        return int(number)
    except:
        return None


def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        gooddata = []
        baddata = []
        count = 0
        #COMPLETE THIS FUNCTION
        #iterate each row - convert XML datetime to year
        for each_row in reader:
            #discard first three rows
            count += 1
            if count < 4:
                continue
            #discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
            #    only process if it has dbpedia in URI

            if each_row["URI"].find('dbpedia.org'):
                #convert XML date to year
                each_row["productionStartYear"] = each_row["productionStartYear"][0:4]
                #print each_row["productionStartYear"]
                #check if in valid range and put in appropriate good/bad dictionary
                year = get_number(each_row["productionStartYear"])
                #print year
                if 1885 < year < 2015:
                    gooddata.append(each_row)
                else:
                    baddata.append(each_row)
        #print 'baddata: ', len(baddata)
        #print 'gooddata: ', len(gooddata)

    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    #write good data file
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        for row in gooddata:
            writer.writerow(row)
    #write bad data file
    with open(output_bad, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        for row in baddata:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()