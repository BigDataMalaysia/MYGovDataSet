#!/usr/bin/python
import mygovdataset

datasets = list()
for dataset_id in range(0, 122):
    url = "http://data.gov.my/view.php?view={0}".format(dataset_id)
    try:
        some_data_set = mygovdataset.MYGovDataSet(url)
        datasets.append(some_data_set)
    except:
        print "id {0} didn't work out".format(dataset_id)

datasets.sort(key=lambda x: x.view_count, reverse=True)

for dataset in datasets:
    print "---------- last updated: {0} views: {1} ----------".format(dataset.last_updated, dataset.view_count)
    print dataset.org_metadata
    print "--------------------------------------------------------------------------------"
