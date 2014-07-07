#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import pprint
import re
import datetime
import string

class MYGovDataSet:

    def __init__(self, url):
        self.url = url
        soup = BeautifulSoup(urllib2.urlopen(self.url).read())
        self.org_metadata = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="view-b")
        update_view_download = soup.findAll('td',{'class':'last'})
        assert len(update_view_download) == 1, "fuckers changed their layout, unexpected: {0}".format(update_view_download)
        update_view_download_string = str(update_view_download[0].text)

        m = re.search("Last Updated :\s*([0-9]+)-([0-9]+)-([0-9]+)\s*([0-9]+):([0-9]+):([0-9]+)\s*\|", update_view_download_string)
        year = int(m.group(1))
        month = int(m.group(2))
        day = int(m.group(3))
        hour = int(m.group(4))
        minute = int(m.group(5))
        second = int(m.group(6))
        self.last_updated = datetime.datetime(year, month, day, hour, minute, second)

        m = re.search("Viewed :([0-9]+)", update_view_download_string)
        self.view_count = int(m.group(1))

datasets = []
for dataset_id in range(0, 200):
    url = "http://data.gov.my/view.php?view={0}".format(dataset_id)
    try:
        some_data_set = MYGovDataSet(url)
        print "{0}: last updated: {1} views: {2}".format(dataset_id, some_data_set.last_updated, some_data_set.view_count)
        datasets.append(some_data_set)
    except:
        print "id {0} didn't work out".format(dataset_id)

datasets.sort(key=lambda x: x.view_count)

for dataset in datasets:
    print "---------- last updated: {0} views: {1} ----------".format(some_data_set.last_updated, some_data_set.view_count)
    print some_data_set.org_metadata
    print "--------------------------------------------------------------------------------"
