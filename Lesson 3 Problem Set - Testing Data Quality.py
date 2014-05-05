__author__ = 'Dad'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some
particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
          "areaLand", "areaMetro", "areaUrban"]

def int_type(n):
    try:
        return int(n)
    except ValueError:
        return False

def float_type(n):
    try:
        return float(n)
    except ValueError:
        return False

def audit_file(filename, fields):
    fieldtypes = {}
    for eachfield in fields:
        fieldtypes[eachfield] = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        count = 0
        for eachline in reader:
            count += 1
            if count < 4:
                continue
            for eachfield in fields:
                if eachline[eachfield] == 'NULL' or eachline[eachfield] == '':
                    #print 'found a null'
                    fieldtypes[eachfield].append(type(None))
                elif eachline[eachfield][0] == '{':
                    #print 'found a list'
                    fieldtypes[eachfield].append(type([]))
                elif int_type(eachline[eachfield]):
                    #print 'found an INT'
                    fieldtypes[eachfield].append(type(1))
                elif float_type(eachline[eachfield]):
                    #print 'found a FLOAT'
                    fieldtypes[eachfield].append(type(1.1))
                else:
                    fieldtypes[eachfield].append(type('str'))

    for key, value in fieldtypes.iteritems():
        fieldtypes[key] = set(fieldtypes[key])
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
