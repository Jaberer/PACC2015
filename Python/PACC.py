import datetime
import csv
from math import radians, cos, sin, asin, sqrt



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

def getPlayerDataArray(string, type):
	filename = folderHeader
	if type == 0:
		filename = filename + player
	elif type == 1:
		filename = filename + team
	else:
		return []
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
			if row[0] != '':
				tmplist.append(row)
	tmplist.remove(tmplist[0])
	# tmplist.remove(tmplist[len(tmplist)-1])
	return tmplist

#http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def listMean(list):
	return sum(list) / len(list)