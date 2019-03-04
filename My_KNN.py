import DistanceType
import operator

#Get neighbors
def getNeighbors(trainingSet, testInstance, num_neighbors, distancetype, *args):
	distances = []
	length = len(testInstance)-1
	for i in range(len(trainingSet)):
		if distancetype == "Euclidean":
			dist = DistanceType.EuclideanDistance(testInstance, trainingSet[i], length)
		elif distancetype == "Manhattan":
			dist = DistanceType.ManhattanDistance(testInstance, trainingSet[i], length)
		else:
			dist = DistanceType.MinkowskiDistance(testInstance, trainingSet[i], length, *args)
		distances.append((trainingSet[i],dist))
	distances.sort(key=operator.itemgetter(1))
	#return distances
	neighbors = []
	for x in range(num_neighbors):
		neighbors.append(distances[x][0])
	return neighbors

#Classification from neighbors (Classification problem)
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

#Regression by taking mean from neighbors (Regression problem)
def getRegression(neighbors):
	output_values = [row[-1] for row in neighbors]
	return sum(output_values) / float(len(output_values))