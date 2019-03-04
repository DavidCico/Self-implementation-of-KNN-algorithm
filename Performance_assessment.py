### Methods to assess accuracy of prediction ####
from math import sqrt

####### Accuracy for classification problems ######

# Get accuracy of prediction #
def getAccuracy(actual,predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i][-1] == predicted[i]:
			correct += 1
	return (correct / float(len(actual))) * 100.00

# Calculate a Confusion Matrix #	
def confusion_matrix(actual, predicted):
	unique = set([row[-1] for row in actual])
	matrix = [list() for x in range(len(unique))]
	for i in range(len(unique)):
		matrix[i] = [0 for x in range(len(unique))]
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for i in range(len(actual)):
		x = lookup[actual[i][-1]]
		y = lookup[predicted[i]]
		matrix[x][y] += 1
	return unique, matrix

# Printing a confusion matrix
def print_confusion_matrix(unique, matrix):
	print('Unique prediction values:')
	print('(P)' + ' '.join(str(x) for x in unique))
	print('(A)---')
	print("Confusion Matrix:")
	for i, x in enumerate(unique):
		print("%s| %s" % (x, ' '.join(str(x) for x in matrix[i])))

# Recall classification estimator #
def recall_precision_calc(matrix):
    for i in range(len(matrix[0])):
        row_values = matrix[i] # row values of matrix
        col_values = [row[i] for row in matrix] # column values of matrix
        tp = col_values[i]
        fp = sum(row_values)-row_values[i] # sum all row values - ones in diagonal
        fn = sum(col_values)-col_values[i] # sum all col values - ones in diagonal
    
    recall = tp / (tp + fn)
    precision = tp / (tp + fp)
    
    F1_score = 2 * (precision * recall) / (precision + recall)
    
    return recall, precision, F1_score
	


		


###### Accuracy methods for Regression problems ########

# Calculate mean absolute error (MAE) #
def mae_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		sum_error += abs(predicted[i] - actual[i][-1])
	return sum_error / float(len(actual))

# Calculate root mean squared error #
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i][-1]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

