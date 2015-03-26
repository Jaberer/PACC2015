import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv
import PACC
from scipy import stats


vMatches = PACC.getPlayerDataArray(string=1, type=1)
sMatches = PACC.getPlayerDataArray(string=0, type=1)

vPlayer = PACC.getPlayerDataArray(string=1, type=0)
sPlayer = PACC.getPlayerDataArray(string=0, type=0)

vMDates = []
sMDates = []

for element in vMatches:
	vMDates.append(datetime.datetime.strptime(element[1], '%m/%d/%Y'))
for element in sMatches:
	sMDates.append(datetime.datetime.strptime(element[1], '%m/%d/%Y'))

gameList = []
normList = []

def addHours(list, matches):
	for element in list:
		if datetime.datetime.strptime(element[2], '%m/%d/%Y') in matches:
			gameList.append(float(element[8]))
		else:
			normList.append(float(element[8]))
addHours(vPlayer, vMDates)
addHours(sPlayer, sMDates)

print sum(gameList)/len(gameList)
print sum(normList)/len(normList)
print stats.ttest_ind(normList, gameList, axis=0, equal_var=False)


binList = np.arange(min([min(gameList), min(normList)]), max([max(gameList), max(normList)]) + 1, 1)

plt.figure()
plt.xlabel('Hours of sleep')
plt.ylabel('Frequency')
plt.title('Hours of Sleep: Before Gameday and Not Gameday')
plt.hist(gameList, bins= binList, color = 'b', histtype = 'stepfilled', normed = True, alpha = 1, label = 'Gameday')
plt.hist(normList, bins = binList, color = 'r', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Non-gameday')
plt.legend()
pylab.savefig('Graphs\\5.png')