#!/usr/bin/python
import mygovdataset
import pprint

FAILS_IN_A_ROW_LIMIT = 10
datasets = list()
dataset_id = 0
fails_in_a_row = 0
while fails_in_a_row < FAILS_IN_A_ROW_LIMIT:
    url = "http://data.gov.my/view.php?view={0}".format(dataset_id)
    try:
        some_data_set = mygovdataset.MYGovDataSet(url)
        fails_in_a_row = 0
        datasets.append(some_data_set)
        print "id {0} added to list".format(dataset_id, e)
    except Exception, e:
        print "WARNING: id {0} didn't work out; exception: {1}".format(dataset_id, e)
        fails_in_a_row += 1
    dataset_id += 1
print "Got {0} fails in a row; assuming there are no more valid data sets (count: {1})".format(FAILS_IN_A_ROW_LIMIT, len(datasets))

#asset_type_counts = dict()
for dataset in datasets:
    print "---------- updated: {0} views: {1} ----------".format(dataset.last_updated, dataset.view_count)
    print dataset.org_metadata
    print dataset.asset_type
    #if dataset.asset_type in asset_type_counts:
    #    asset_type_counts[dataset.asset_type] += 1
    #else:
    #    asset_type_counts[dataset.asset_type] = 1

#print "\n\nASSET TYPES:\n\t{0}".format(asset_type_counts)
