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
from My_KNN import getResponse

#Accuracy of the predictions
from Performance_assessment import getAccuracy
from Performance_assessment import confusion_matrix
from Performance_assessment import print_confusion_matrix
from Performance_assessment import recall_precision_calc

def main():

	# Load iris dataset
	filename = 'iris.csv'
	dataset = load_csv(filename)
	print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
	print(dataset[0])

	# convert string columns to float
	for i in range(4):
		str_column_to_float(dataset, i)
	# convert class column to int
	lookup = str_column_to_int(dataset, 4)
	print(dataset[0])
	print(lookup)

	# normalization of dataset
	minmax = dataset_minmax(dataset)
	Normalize_Dataset(dataset, minmax)

	# Splitting dataset between Training and Testing Set
	split = 0.6
	trainingSet, testSet = train_test_split(dataset, split)

	#generate predictions
	predictions = []
	num_neighbors = 3
	for i in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[i], num_neighbors, "Euclidean")
		classify = getResponse(neighbors)
		predictions.append(classify)
		print('> predicted=' + repr(classify) + ', actual=' + repr(testSet[i][-1]))

	#Accuracy Assessment
	accuracy = getAccuracy(testSet,predictions)
	print('Accuracy :' + repr(accuracy) + '%')
	unique, matrix = confusion_matrix(testSet, predictions)

	print('\n')
	print_confusion_matrix(unique, matrix)
	print('\n')

	#Calculate properties for recall and precision
	Recall, Precision, F1_score = recall_precision_calc(matrix)
	print('Recall:', Recall)
	print('Precision:', Precision)
	print('F1 score:', F1_score)



main()



