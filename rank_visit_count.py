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
        datasets.append({"dataset" : some_data_set, "dataset_id" : dataset_id})
        print "id {0} added to list".format(dataset_id, e)
    except Exception, e:
        print "WARNING: id {0} didn't work out; exception: {1}".format(dataset_id, e)
        fails_in_a_row += 1
    dataset_id += 1
print "Got {0} fails in a row; assuming there are no more valid data sets (count: {1})".format(FAILS_IN_A_ROW_LIMIT, len(datasets))

# sort by view count, highest to lowest
datasets.sort(key=lambda x: x["dataset"].view_count, reverse=True)

rank = 1
print "#rank, id, view_count"
for dataset in datasets:
    print "{0}, {1}, {2}".format(rank, dataset["dataset_id"], dataset["dataset"].view_count)
    rank += 1
