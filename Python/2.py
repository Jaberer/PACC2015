import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv
from scipy import stats

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

with open('C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_volleyball.csv', 'rb') as soccerFile:
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
plt.hist(weekList, bins=binlist, normed=1, facecolor='green', alpha=1, label='Weekdays')
plt.hist(weekendList, bins=binlist, normed=1, facecolor='blue', alpha=0.5, label='Weekends')
plt.legend(bbox_to_anchor=(0.45, 0.9), bbox_transform=plt.gcf().transFigure)
plt.xlabel('Hours of sleep')
plt.ylabel('Frequency')
plt.title('Sleep per night distribution on weekdays vs. weekends')
pylab.savefig('Graphs/weekdayDist.png')


print listAverage(weekList), listAverage(weekendList)

print stats.ttest_ind(weekList, weekendList, axis=0, equal_var=False)

