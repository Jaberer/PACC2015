import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import PACC


sTList = PACC.getGameDates(0)
vTList = PACC.getGameDates(1)

sPArray = PACC.getPlayerDataArray(0)
vPArray = PACC.getPlayerDataArray(1)

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
plt.hist(gameDist, bins = 5, color = 'b', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Gameday')
plt.hist(normDist, bins = 5, color = 'r', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Not Gameday')
pylab.savefig('Graphs\\6.png')

print sum(gameDist)/len(gameDist), sum(normDist)/len(normDist)
