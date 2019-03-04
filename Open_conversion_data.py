import csv
import random
from math import sqrt


## Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = csv.reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

## Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

## Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup


##### Normalize Data ###########

# Find the min and max values for each column

def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		colvalues = [row[i] for row in dataset]
		min_value = min(colvalues) 
		max_value = max(colvalues)
		minmax.append([min_value, max_value])
	return minmax

# Normalize the dataset except last row for classification values
def Normalize_Dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)-1):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


#### Standardize Data ######

# calculate column means
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i] = sum(col_values) / float(len(dataset))
	return means

# calculate column standard deviations
def column_stdevs(dataset, means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		variance = [pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i] = sum(variance)
		stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs]
	return stdevs

# Standardize the dataset
def Standardize_Dataset(dataset, means, stdevs):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - means[i]) / stdevs[i]


