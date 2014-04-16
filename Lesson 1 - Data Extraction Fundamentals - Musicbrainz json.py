__author__ = 'Dad'
# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}

#2
def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    #print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

#1
def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    #print 'params', params
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    #results = query_by_name(ARTIST_URL, query_type["simple"], "queen")
    #print "Query reslts: "
    #pretty_print(results)
    #print '======================================='

    #how many bands named FIRST AID KIT
    results = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
    #print len(results)
    #pretty_print(results)
    fakcount = 0
    for artist in results["artist"]:
        if artist["name"] == "First Aid Kit":
            fakcount += 1
    print "First Aid Kits: ", fakcount


    print "=================================="
    #begin_area for queen
    results = query_by_name(ARTIST_URL, query_type["simple"], "queen")
    #print type(results)
    print "Queen begin location: ",
    pretty_print(results["artist"][0]["begin-area"]["name"])

    #spanish alias for beatles
    results = query_by_name(ARTIST_URL, query_type["simple"], "beatles")
    pretty_print(results)

    q3 = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    aliases = q3["artist"][0]["aliases"]
    alias = ''
    for a in aliases:
        if a["locale"] == "es":
            alias = a["name"]
    print "Q3: Spanish alias for Beatles"
    print alias
    #pretty_print(q3)

    q4 = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    disam = q4["artist"][0]["disambiguation"]
    print "Q4: Disambiguation Nirvana"
    print disam

    q5 = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    begin_date = q5["artist"][0]["life-span"]["begin"]
    print "Q5: One Direction begin"
    print begin_date
    #nirvana disambiguation
    #when was one direction formed?


    #artist_id = results["artist"][1]["id"]
    #print "\nARTIST:"
    #pretty_print(results["artist"][1])
    #
    #artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    #releases = artist_data["releases"]
    #print "\nONE RELEASE:"
    #pretty_print(releases[0], indent=2)
    #release_titles = [r["title"] for r in releases]
    #
    #print "\nALL TITLES:"
    #for t in release_titles:
    #    print t


if __name__ == '__main__':
    main()
