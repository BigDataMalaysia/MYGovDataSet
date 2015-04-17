'''
Das Class
'''
import urllib2
from bs4 import BeautifulSoup
import re
import datetime

class MYGovDataSet:

    def __init__(self, url, payload_text=None):
        '''
        The conventional initialization method is to provide the target url and let the object do it's own fetching, but for testing purposes a payload can be provided directly, in which case the url is ignored (not even saved).
        '''
        if payload_text:
            self.url = None
            payload = payload_text
        else:
            self.url = url
            payload = urllib2.urlopen(self.url).read()
        soup = BeautifulSoup(payload)

        self.org_metadata = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="view-b")
        update_view_download = soup.findAll('td',{'class':'last'})
        if len(update_view_download) != 1:
            raise Exception("unexpected layout, got update_view_download: {0}".format(update_view_download))

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

        download = update_view_download[0].findAll('a',{'target':'_blank'})
        self.asset_url = []
        self.ico_file = []
        self.asset_type = []
        if len(download) > 1:
            print "WARNING: Multiple assets discovered"
        for asset_number in range(0, len(download)):
            self.asset_url.append(download[asset_number].get('href'))
            self.ico_file.append(download[asset_number].contents[0].get('src'))
            if 'ico-pdf' in self.ico_file[-1]:
                asset_type = "PDF"
            elif 'ico-excel' in self.ico_file[-1]:
                asset_type = "XLS"
            elif 'ico-csv' in self.ico_file[-1]:
                asset_type = "CSV"
            elif 'ico-web' in self.ico_file[-1]:
                asset_type = "WEB"
            else:
                print "WARNING: Unknown asset type (ico file: {0}, asset_url: {1})".format(self.ico_file[-1], self.asset_url[-1])
                asset_type = "UNKNOWN"
            self.asset_type.append(asset_type)
