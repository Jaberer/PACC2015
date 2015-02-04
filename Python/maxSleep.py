import csv
import time
import datetime

soccerDict = {}
recordDict = {}
minDate = 0
maxDate = 0

with open('C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_soccer.csv', 'rb') as soccerFile:
		reader = csv.reader(soccerFile, delimiter = ',')
		for row in reader:
			try:
				if row[0] in soccerDict:
					soccerDict[row[0]] = soccerDict[row[0]] + int(row[8])
					recordDict[row[0]] += 1
				else:
					soccerDict[row[0]] = int(row[8])
					recordDict[row[0]] = 1
			except:
				next
			



maxSleep = 0
maxID = 0
totalHours = 0
for key in soccerDict.keys():
	if soccerDict[key] / recordDict[key] > maxSleep:
		maxSleep = soccerDict[key] / recordDict[key]
		totalHours = soccerDict[key]
		maxID = key
print "max sleep: %d\nID : %s\nTotal sleep: %d" % (maxSleep, maxID, totalHours)