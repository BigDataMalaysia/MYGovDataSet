#!/usr/bin/python
import mygovdataset

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
    except Exception, e:
        print "id {0} didn't work out; exception: {1}".format(dataset_id, e)
        fails_in_a_row += 1
    dataset_id += 1
print "Got {0} fails in a row; assuming there are no more valid data sets (count: {1})".format(FAILS_IN_A_ROW_LIMIT, len(datasets))

# sort by view count, highest to lowest
datasets.sort(key=lambda x: x.view_count, reverse=True)

for dataset in datasets:
    print "---------- last updated: {0} views: {1} ----------".format(dataset.last_updated, dataset.view_count)
    print dataset.org_metadata
    print "--------------------------------------------------------------------------------"
