__author__ = 'dad'
import urllib2

#link to get the html file
page = urllib2.urlopen('http://esp1.pristine.com/ppsn/_PPSNTopListResult.php?new_request=1&FromPrice=10&ToPrice='
                       '&FromVolume=1000000&ScanInfoID=111')

page_content = page.read()

with open('pristine_daily_setup_content.html', 'w') as fid:
    fid.write(page_content)

