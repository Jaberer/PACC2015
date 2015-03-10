import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import PACC

socAfterGameDay = []
for x in PACC.getGameDates(0):
	socAfterGameDay.append(x + datetime.timedelta(days = 1))
socSore = []
for element in PACC.getPlayerDataArray(string = 0, type = 0):
	try:
		date = datetime.datetime.strptime(element[2], '%m/%d/%Y')
	except:
		pass
	if date in socAfterGameDay:
		socSore.append(int(element[5]))

volAfterGameDay = []
for x in PACC.getGameDates(1):
	volAfterGameDay.append(x + datetime.timedelta(days = 1))
volSore = []
for element in PACC.getPlayerDataArray(string = 1, type = 0):
	try:
		date = datetime.datetime.strptime(element[2], '%m/%d/%Y')
	except:
		pass
	if date in volAfterGameDay:
		volSore.append(int(element[5]))
plt.figure()
plt.xlabel('Soreness after Game')
plt.ylabel('Frequency')
plt.title('Post-Game Soreness: Volleyball vs. Soccer')
plt.hist(socSore, bins = 5, color = 'b', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Soccer')
plt.hist(volSore, bins = 5, color = 'r', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Volleyball')
plt.xticks(np.arange(1, 6, 1.0))
plt.legend()
pylab.savefig('Graphs\\8.png')