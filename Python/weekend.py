import numpy as np
import matplotlib.pyplot as plt
import datetime
import csv

def addToDict(dict, key):
	if key in dict:
		dict[key] += 1
	else:
		dict[key] = 1
	return


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
				addToDict(weekendDist, int(row[8]))
				weekendList.append(row[8])
			else:
				addToDict(weekDist, int(row[8]))
				weekList.append(row[8])
		except:
			next


weekHist = np.histogram(np.array(weekendList), 9)
