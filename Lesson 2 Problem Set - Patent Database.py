#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    # we want you to split the input file into separate files
    # each containing a single patent.
    # As a hint - each patent declaration starts with the same line that was causing the error
    # The new files should be saved with filename in the following format:
    # "{}-{}".format(filename, n) where n is a counter, starting from 0.
    #
    filenumber = 0
    startline = '<?xml version="1.0" encoding="UTF-8"?>'
    firstline = True
    #open file
    filecontent = ''
    f = open(filename, "r")
    while True:
        line = f.readline()
        #were at end of file so exit wjile loop
        if not line:
            break

        #if we find a newfile line, write current contents to file and start again
        if startline == line.rstrip("\r\n") and firstline is False:
            with open("{}-{}".format(filename, filenumber), "w") as of:
                of.write(filecontent)
            filecontent = ''
            filenumber += 1

        filecontent += line
        #set firstline to false after first line is read
        firstline = False
    #write final file
    with open("{}-{}".format(filename, filenumber), "w") as of:
                of.write(filecontent)
    f.close()
    return


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)
    print 'all done'

test()