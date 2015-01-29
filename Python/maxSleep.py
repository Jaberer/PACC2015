import csv
import re

soccerDict = {}
minDate = 0
maxDate = 0


with open('C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_soccer.csv', 'rb') as soccerFile:
		reader = csv.reader(soccerFile, delimiter = ',')
		pattern = r'[-+]?\d+\\[-+]?\d+\\'
		for row in reader:
			try:
				if row[0] in soccerDict:
					soccerDict[row[0]] = soccerDict[row[0]] + int(row[8])
				else:
					soccerDict[row[0]] = int(row[8])
			except:
				next
			if re.match(pattern, row[2]):
				print row[2]
				



maxSleep = 0
maxID = 0
for key in soccerDict.keys():
	if soccerDict[key] > maxSleep:
		maxSleep = soccerDict[key]
		maxID = key
print maxSleep, maxID