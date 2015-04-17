#!/usr/bin/python
import pandas
import csv
import pprint

old_csv_file_name = "viewcount_25-OCT-2014.csv"
new_csv_file_name = "viewcount_07-APR-2015.csv"
old_data = pandas.read_csv(old_csv_file_name, skipinitialspace=True)
new_data = pandas.read_csv(new_csv_file_name, skipinitialspace=True)

old_data_ids = set(old_data['id'])
new_data_ids = set(new_data['id'])

new_data_sets = new_data_ids - old_data_ids
removed_data_sets = old_data_ids - new_data_ids

print "New data sets: {} (total count: {})".format(new_data_sets, len(new_data_sets))
print "Removed data sets: {} (total count: {})".format(removed_data_sets, len(removed_data_sets))
