'''
Das Class
'''
import urllib2
from bs4 import BeautifulSoup
import re
import datetime

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
