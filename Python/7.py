import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
#import urllib
import xml.etree.ElementTree as etree
import PACC
from scipy import stats

sTArray = PACC.getPlayerDataArray(type = 1, string = 0)
vTArray = PACC.getPlayerDataArray(type = 1, string = 1)

data = []


for element in sTArray:
	if element[3] == 'A':
		data.append([element[1], 'soccer', 'away', element[4], []])
	elif element[3] == 'H':
		data.append([element[1], 'soccer', 'home', element[4], []])
for element in vTArray:
	if element[3] == 'A':
		data.append([element[1], 'volleyball', 'away', element[4], []])	
	elif element[3] == 'H':
		data.append([element[1], 'volleyball', 'home', element[4], []])

sPArray = PACC.getPlayerDataArray(type = 0, string = 0)
vPArray = PACC.getPlayerDataArray(type = 0, string = 1)

for x in data:
	for element in sPArray:
		if x[0] == element[2] and x[1] == 'soccer':
			x[4].append(int(element[6]))
	for element in vPArray:
		if x[0] == element[2] and x[1] == 'volleyball':
			x[4].append(int(element[6]))

hHist = []
aHist = []

for element in data:
	if element[2] == 'away':
		for datum in element[4]:
			aHist.append(int(datum))
	else:
		for datum in element[4]:
			hHist.append(int(datum))


queryPrefix = 'https://maps.googleapis.com/maps/api/place/textsearch/xml?query='
queryKey = '&key=AIzaSyA-VLpKvAEL5CGdsoOgS5yBva56w_FylPo'

for element in data:
	#placeName = element[3].replace(' ', '+')
	#queryURL = queryPrefix + placeName + queryKey
	#queryXML = urllib.urlretrieve(url = queryURL, filename = 'XML\\' + element[3] + '.xml')
	
	tree = etree.parse('XML\\' + element[3] + '.xml')
	root = tree.getroot()
	lat = float(root[1][4][0][0].text)
	long = float(root[1][4][0][1].text)
	element.append(lat)
	element.append(long)

homeCoord = []
for element in data:
	if element[3] == 'Seattle, WA':
		homeCoord.append(float(element[5]))
		homeCoord.append(float(element[6]))
		break

for element in data:
	element.append(PACC.haversine(lon1 = element[6], lon2 = homeCoord[1], lat1 = element[5], lat2 = homeCoord[0]))
	print element[len(element) - 1]

distance = []
meanStress = []
for element in data:
	if element[7] > 20:
		try:
			meanStress.append(stats.mode(element[4])[0])
			distance.append(element[7])
		except:
			next
	
colors = np.random.rand(50)

plt.figure()
plt.scatter(distance, meanStress, alpha=1)
plt.xlabel('Distance from Home (km)')
plt.ylabel('Average Stress')
plt.yticks([0, 1, 2, 3, 4, 5])
plt.title('Distance vs. Stress')
pylab.savefig('Graphs\\7scatter.png')

	
plt.figure()
plt.xlabel('Stress Level')
plt.ylabel('Frequency')
plt.title('Stress: Home vs. Away')
plt.hist(hHist, bins = [1, 2, 3, 4, 5, 6], color = 'b', normed = True, alpha = 1, label = 'Home')
plt.hist(aHist, bins = [1, 2, 3, 4, 5, 6], color = 'r', normed = True, alpha = 0.5, label = 'Away')
plt.legend(bbox_to_anchor=(0.4, 0.9), bbox_transform=plt.gcf().transFigure)

pylab.savefig('Graphs\\7.png')


print "Averages"
print stats.mode(hHist), stats.mode(aHist)
print stats.ks_2samp(hHist, aHist)