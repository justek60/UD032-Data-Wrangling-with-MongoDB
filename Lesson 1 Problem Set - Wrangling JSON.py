#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This exercise shows some important concepts that you should be aware about:
- using codecs module to write unicode files
- using authentication with web APIs
- using offset when accessing web APIs

To run this code locally you have to register at the NYTimes developer site
and get your own API key. You will be able to complete this exercise in our UI without doing so,
as we have provided a sample result.

Your task is to process the saved file that represents the most popular (by view count)
articles in the last day, and return the following data:
- list of dictionaries, where the dictionary key is "section" and value is "title"
- list of URLs for all media entries with "format": "Standard Thumbnail"

All your changes should be in the article_overview function.
The rest of functions are provided for your convenience, if you want to access the API by yourself.
"""
import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": "",
            "article": ""}

def pretty_print(data, indent=4):
    print type(data)
    if type(data) == list:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data

def get_from_file(kind, period):
    filename = "popular-{0}-{1}.json".format(kind, period)
    with open(filename, "r") as f:
        return json.loads(f.read())


def article_overview(kind, period):
    data = get_from_file(kind, period)
    #data is a list of dictionaries
    #pretty_print(data)
    titles = []
    urls =[]
    #- return a list of dictionaries, where the dictionary key is "section" and value is "title"
    for each_article in data:
        for (key, value) in each_article.items():
            if key == 'section':
                #print (key, value)
                titles.append({each_article['section']: each_article['title']})

    #- return a list of URLs for all media entries with "format": "Standard Thumbnail"
    #data is a list of dictionaries. Each dictionary is one article and its data
    for each_article in data:
        #each_article['media'] is a list of dictionaries. each dict is a list medias
        for each_media in each_article['media']:
            #each_media is a dictionary of medias. each dict is a medias data
            #each media-metadata is a list of dictionaries. Each dict is the metadata info
            for each_metadata in each_media['media-metadata']:
                if each_metadata['format'] == "Standard Thumbnail":
                    urls.append(each_metadata['url'])

    #print len(urls)
    # YOUR CODE HERE

    return (titles, urls)


def query_site(url, target, offset):
    # This will set up the query with the API key and offset
    # Web services often use offset paramter to return data in small chunks
    # NYTimes returns 20 articles per request, if you want the next 20
    # You have to provide the offset parameter
    if API_KEY["popular"] == "" or API_KEY["article"] == "":
        print "You need to register for NYTimes Developer account to run this program."
        print "See Intructor notes for information"
        return False
    params = {"api-key": API_KEY[target], "offset": offset}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def get_popular(url, kind, days, section="all-sections", offset=0):
    # This function will construct the query according to the requirements of the site
    # and return the data, or print an error message if called incorrectly
    if days not in [1,7,30]:
        print "Time period can be 1,7, 30 days only"
        return False
    if kind not in ["viewed", "shared", "emailed"]:
        print "kind can be only one of viewed/shared/emailed"
        return False

    url = URL_POPULAR + "most{0}/{1}/{2}.json".format(kind, section, days)
    data = query_site(url, "popular", offset)

    return data


def save_file(kind, period):
    # This will process all results, by calling the API repeatedly with supplied offset value,
    # combine the data and then write all results in a file.
    data = get_popular(URL_POPULAR, "viewed", 1)
    num_results = data["num_results"]
    full_data = []
    with codecs.open("popular-{0}-{1}-full.json".format(kind, period), encoding='utf-8', mode='w') as v:
        for offset in range(0, num_results, 20):
            data = get_popular(URL_POPULAR, kind, period, offset=offset)
            full_data += data["results"]

        v.write(json.dumps(full_data, indent=2))


def test1():
    titles, urls = article_overview("viewed", 1)
    assert len(titles) == 20
    assert len(urls) == 30
    assert titles[2] == {'Opinion': 'Professors, We Need You!'}
    assert urls[20] == 'http://graphics8.nytimes.com/images/2014/02/17/sports/ICEDANCE/ICEDANCE-thumbStandard.jpg'


if __name__ == "__main__":
    test1()
