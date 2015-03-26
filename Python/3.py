import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv
import PACC

def listAverage(list):
	sum = 0
	for element in list:
		sum += float(element)
	return sum / len(list)
sleepList = []
minID = []
maxID = []


socArray = PACC.getPlayerDataArray(string=0, type=0)

maxVal = 0
minVal = -1

for element in socArray:
	sleepList.append(float(element[8]))
	if max(sleepList) > maxVal:
		del maxID[:]
		maxID.append(int(element[0]))
		maxVal = max(sleepList)
	elif float(element[8]) == maxVal:
		maxID.append(int(element[0]))
	if minVal == -1:
		minVal = min(sleepList)
		minID.append(int(element[0]))
	elif minVal > min(sleepList):
		del minID[:]
		minID.append(int(element[0]))
		minVal = min(sleepList)
	elif minVal == float(element[8]):
		minID.append(int(element[0]))



print listAverage(sleepList), min(sleepList), max(sleepList), set(maxID), set(minID), sleepList

plt.figure()
n, bins, patches = plt.hist(sleepList, bins=range(int(min(sleepList)), int(max(sleepList)) + 1, 1), normed=0, facecolor='green', alpha=1)
plt.xlabel('Hours of sleep')
plt.ylabel('Number of occurrences')
plt.rcParams["axes.titlesize"] = 10
plt.title('Sleep per night distribution of volleyball players')
pylab.savefig('Graphs/volleyballSleep.png')

