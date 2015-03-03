import datetime
import csv


__name__ = 'PACC'

folderHeader = 'C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\'
player = 'player_data_'
team = 'team_results_'
fileExt = '.csv'
soc = 'soccer'
vlybl = 'volleyball'


def getGameDates(string):
	filename = folderHeader + team
	if string == 0:
		filename = filename + soc
	elif string == 1:
		filename = filename + vlybl
	else:
		return []
	filename = filename + fileExt
	tmplist = []
	with open(filename, 'rb') as file:
		gameread = csv.reader(file, delimiter = ',')
		for row in gameread:
			try:
				tmplist.append(datetime.datetime.strptime(row[1], "%m/%d/%Y"))
			except:
				next
		return tmplist

def getPlayerDataArray(string):
	filename = folderHeader + player
	if string == 0:
		filename = filename + soc
	elif string == 1:
		filename = filename + vlybl
	else:
		return []
	filename = filename + fileExt
	tmplist = []
	with open(filename, 'rb') as file:
		gameread = csv.reader(file, delimiter = ',')
		for row in gameread:
			tmplist.append(row)
	tmplist.remove(tmplist[0])
	return tmplist

