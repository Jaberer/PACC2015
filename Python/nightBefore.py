import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv

def graphList(list, name):
	plt.figure()
	plt.xlabel('Hours of sleep')
	plt.ylabel('Occurences')
	plt.title(name)
	n, bins, patches = plt.hist(list, bins = int(max(list) + 1), range = (int(min(list) - 1), int(max(list) + 1))) 
	pylab.savefig(name + '.png')

def getEventList(filename):
	socDateList = []
	with open(filename, 'rb') as socTeamFile:
		socRead = csv.reader(socTeamFile, delimiter = ',')
		for row in socRead:
			try:
				socDateList.append(datetime.datetime.strptime(row[1], "%m/%d/%Y") - datetime.timedelta(days = 1))
			except:
				next
	return socDateList

def checkEventList(filename, eventList, num):
	gameSlp = []
	normSlp = []
	with open(filename, 'rb') as soccerFile:
		soccerRead = csv.reader(soccerFile, delimiter = ',')
		for row in soccerRead:
			try:
				tmp = datetime.datetime.strptime(row[2], "%m/%d/%Y")
				if tmp in eventList:
					gameSlp.append(float(row[num]))
				else:
					normSlp.append(float(row[num]))
			except:
				next
	return normSlp, gameSlp

def graphFile(filename, eventfilename, name, num):
	tb1, tb2 = checkEventList(filename, getEventList(eventfilename), num)
	graphList(tb1, "%s %d" % (name, 1))
	graphList(tb2, "%s %d" % (name, 2))



playerSoccerData = 'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_soccer.csv'
teamSoccerData =  'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\team_results_soccer.csv' 
playerVolleyballData = 'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_volleyball.csv'
teamVolleyballData = 'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\team_results_volleyball.csv'
graphFile(playerSoccerData, teamSoccerData, 'soccerdat', 8)
graphFile(playerVolleyballData, teamVolleyballData, 'volleyballdat', 8)
graphFile(playerSoccerData, teamSoccerData, 'soccerdatStress', 6)
graphFile(playerVolleyballData, teamVolleyballData, 'volleyballdatStress', 6)




