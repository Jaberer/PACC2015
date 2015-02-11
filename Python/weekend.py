import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv

def addToDict(dict, key):
	if key in dict:
		dict[key] += 1
	else:
		dict[key] = 1
	return

def listAverage(list):
	sum = 0
	for element in list:
		sum += float(element)
	return sum / len(list)

weekendDist = {}
weekDist = {}
weekendList = []
weekList = []

with open('C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_soccer.csv', 'rb') as soccerFile:
	soccerRead = csv.reader(soccerFile, delimiter = ',')
	for row in soccerRead:
		try:
			day = datetime.datetime.strptime(row[2], "%m/%d/%Y").weekday()			
			if int(day) == 5 or int(day) == 6:
				addToDict(weekendDist, float(row[8]))
				weekendList.append(float(row[8]))
			else:
				addToDict(weekDist, float(row[8]))
				weekList.append(float(row[8]))
		except:
			next


binlist = []
count = 1
while count <= len(weekDist):
	binlist.append(count)
	count += 1

plt.figure()
n, bins, patches = plt.hist(weekList, bins=binlist, normed=0, facecolor='green', alpha=1)
plt.xlabel('Hours of sleep')
plt.ylabel('Occurences')
plt.title('Sleep per night distribution on weekdays (mean: %.01f hours)' % listAverage(weekList))
pylab.savefig('weekdayDist.png')


plt.figure()
n, bins, patches = plt.hist(weekendList, bins=binlist, normed=0, facecolor='blue', alpha=1)
plt.xlabel('Hours of sleep')
plt.ylabel('Occurences')
plt.title('Sleep per night distribution on weekends (mean: %.01f hours)' % listAverage(weekendList))
pylab.savefig('weekendDist.png')



