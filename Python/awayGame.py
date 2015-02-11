import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv
from nightBefore import getEventList
import scipy

playerSoccerData = 'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_soccer.csv'
teamSoccerData =  'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\team_results_soccer.csv' 
playerVolleyballData = 'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_volleyball.csv'
teamVolleyballData = 'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\team_results_volleyball.csv'

def getDateDistance(file):
	result = []
	with open(file, 'rb') as afile:
		read = csv.reader(afile, delimiter = ',')
		for row in read:
			try:
				date = datetime.datetime.strptime(row[1], '%m/%d/%Y')
				if str(row[4]) != 'Seattle, WA':
					result.append(date)
			except:
				next
	return result


def getAverageStress(list, file):
	tmp = []

	with open(file, 'rb') as afile:
		read = csv.reader(afile, delimiter = ',')
		for row in read:
			try:
				date = datetime.datetime.strptime(row[2], '%m/%d/%Y')
				if date in list:
					tmp.append([date, int(row[6])])
			except:
				next
	result = {}
	for element in tmp:
		if element[0] not in result.keys():
			result[element[0]] = [element[1], 1]
		else:
			result[element[0]] = [result[element[0]][0] + element[1], result[element[0]][1] + 1]
	listresult = {}
	for k in result.keys():
		listresult[k] = result[k][0] / result[k][1]
	return listresult

print getAverageStress(getDateDistance(teamSoccerData), playerSoccerData)