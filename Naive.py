import numpy as np
from sklearn.naive_bayes import GaussianNB
import csv
import random

def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	accuracy = 0.0
	split = 0.25
	loadDataset('Dataset/temphumidity.csv', split, trainingSet, testSet)
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
	# generate predictions
	predictions=[]
	trainData = np.array(trainingSet)[:,0:np.array(trainingSet).shape[1] - 1]
  	columns = trainData.shape[1] 
	X = np.array(trainData).astype(np.float)
	y = np.array(trainingSet)[:,columns].astype(np.float)
	clf = GaussianNB()
	clf.fit(X, y)
	testData = np.array(testSet)[:,0:np.array(trainingSet).shape[1] - 1]
	X_test = np.array(testData).astype(np.float)
	y_test = np.array(testSet)[:,columns].astype(np.float)
	accuracy = clf.score(X_test,y_test)
	accuracy *= 100
	print(clf.predict([[1996,8,27]]))
	print("Accuracy %:",accuracy)	



def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)):
	        for y in range(np.array(dataset).shape[1]):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            testSet.append(dataset[x])
	        else:
	            trainingSet.append(dataset[x])


main()	
	

