#!/usr/bin/python
import mygovdataset

with open("dataset53.txt", "r") as dataset_raw:
    dataset = mygovdataset.MYGovDataSet(url=None, payload_text=dataset_raw.read())

print dataset

print "---------- updated: {0} views: {1} ----------".format(dataset.last_updated, dataset.view_count)
print dataset.org_metadata
print "Asset URL: {0}".format(dataset.asset_url)
print "Asset type: {0}".format(dataset.asset_type)
