import math

#Euclidean Distance
def EuclideanDistance(instance1, instance2, length):
	distance = 0
	for i in range(length):
		distance += pow(instance2[i]-instance1[i],2)
	return math.sqrt(distance)

#Manhattan Distance
def ManhattanDistance(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += abs(instance2[i]-instance1[i])
    return distance

#Minkowski distance with parameter p for power 
def MinkowskiDistance(instance1, instance2, length, p):
    distance = 0
    for i in range(length):
        distance += pow(abs(instance2[i]-instance1[i]), p)
    return pow(distance, 1/p)
