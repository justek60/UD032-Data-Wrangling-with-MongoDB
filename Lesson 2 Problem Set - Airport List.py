__author__ = 'Dad'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html.read())
        carriers = soup.find(id='AirportList')
        for eachoptiontag in carriers.find_all('option'):
            if len(eachoptiontag['value']) < 4 and eachoptiontag['value'] != 'All':
                data.append(eachoptiontag['value'])
        print data
    return data


def test():
    data = extract_airports(html_page)
    print 'Length fo data: ', len(data)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()