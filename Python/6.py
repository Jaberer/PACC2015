import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import PACC
from scipy import stats


sTList = PACC.getGameDates(0)
vTList = PACC.getGameDates(1)

sPArray = PACC.getPlayerDataArray(0, 0)
vPArray = PACC.getPlayerDataArray(1, 0)

gameDist = []
normDist = []

for entry in sPArray:
	date = datetime.datetime.strptime(entry[2], "%m/%d/%Y")
	if date in sTList:
		gameDist.append(int(entry[6]))
	else:
		normDist.append(int(entry[6]))
for entry in vPArray:
	date = datetime.datetime.strptime(entry[2], "%m/%d/%Y")
	if date in vTList:
		gameDist.append(int(entry[6]))
	else:
		normDist.append(int(entry[6]))

plt.figure()
plt.xlabel('Stress Level of Player')
plt.ylabel('Frequency')
plt.title('Stress: Gameday vs. Not Gameday')
plt.hist(gameDist, bins = [1, 2, 3, 4, 5, 6], color = 'b', normed = True, alpha = 1, label = 'Gameday')
plt.hist(normDist, bins = [1, 2, 3, 4, 5, 6], color = 'r', normed = True, alpha = 0.5, label = 'Not Gameday')
plt.legend(bbox_to_anchor=(0.45, 0.9), bbox_transform=plt.gcf().transFigure)

pylab.savefig('Graphs\\6.png')

print sum(gameDist)/len(gameDist), sum(normDist)/len(normDist)

print max(gameDist), max(normDist)

print stats.ks_2samp(gameDist, normDist)