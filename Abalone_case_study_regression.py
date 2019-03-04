#Loading different subroutines for main program

#Import and Conversion, Normalization of Data
from Open_conversion_data import load_csv
from Open_conversion_data import str_column_to_float
from Open_conversion_data import str_column_to_int
from Open_conversion_data import dataset_minmax
from Open_conversion_data import Normalize_Dataset

#Splitting dataset in train, test or folds for cv
from Split_dataset import train_test_split
from Split_dataset import cross_validation_split

#KNN algorithm for classification
from My_KNN import getNeighbors
from My_KNN import getRegression

#RMSE definition for regression analysis
from Performance_assessment import rmse_metric

def main():

	# Load iris dataset
	filename = 'abalone.csv'
	dataset = load_csv(filename)

	# convert string columns to float
	for i in range(1, len(dataset[0])):
		str_column_to_float(dataset, i)
	# convert first column to int
	str_column_to_int(dataset, 0)

	# Splitting dataset between Training and Testing Set
	split = 0.6
	trainingSet, testSet = train_test_split(dataset, split)

	#generate predictions
	predictions = []
	num_neighbors = 3
	for i in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[i], num_neighbors, "Euclidean")
		output = getRegression(neighbors)
		predictions.append(output)
		print('> predicted = %.2f, actual = %.1f' % (output, testSet[i][-1]))

	print('')
	RMSE = rmse_metric(testSet, predictions)
	print('RMSE: %.3f' % RMSE)

main()



