import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv

def listAverage(list):
	sum = 0
	for element in list:
		sum += float(element)
	return sum / len(list)

sleepList = []
minID = []
maxID = []
with open('C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_volleyball.csv', 'rb') as soccerFile:
	reader = csv.reader(soccerFile, delimiter=',')
	for row in reader:
		try:
			sleepList.append(float(row[8]))
		except:
			next
	maxVal = max(sleepList)
	minVal = min(sleepList)
	for row in reader:
		if row[8] == maxVal:
			maxID.append(row[0])
		elif row[8] == minVal:
			minId.append(row[0])

plt.figure()
n, bins, patches = plt.hist(sleepList, bins=range(int(min(sleepList)), int(max(sleepList)) + 1, 1), normed=0, facecolor='green', alpha=1)
plt.xlabel('Hours of sleep')
plt.ylabel('Number of occurrences')
plt.rcParams["axes.titlesize"] = 10
plt.title(r'Sleep per night distribution of volleyball players (mean: %.01f hours, range: %d - %d)' % (listAverage(sleepList), min(sleepList), max(sleepList)))
pylab.savefig('volleyballSleep.png')