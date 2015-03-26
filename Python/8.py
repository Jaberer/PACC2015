import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import PACC
from scipy import stats

socAfterGameDay = []
socNot = []
for x in PACC.getGameDates(0):
	socAfterGameDay.append(x + datetime.timedelta(days = 1))
socSore = []
for element in PACC.getPlayerDataArray(string = 0, type = 0):
	
	date = datetime.datetime.strptime(element[2], '%m/%d/%Y')
	if date in socAfterGameDay:
		socSore.append(int(element[5]))
	else:
		socNot.append(int(element[5]))

volAfterGameDay = []
for x in PACC.getGameDates(1):
	volAfterGameDay.append(x + datetime.timedelta(days = 1))
volSore = []
volNot = []
for element in PACC.getPlayerDataArray(string = 1, type = 0):
	
	date = datetime.datetime.strptime(element[2], '%m/%d/%Y')
	if date in volAfterGameDay:
		volSore.append(int(element[5]))
	else:
		volNot.append(int(element[5]))

plt.figure()
plt.xlabel('Soreness after Game')
plt.ylabel('Frequency')
plt.title('Post-Game Soreness: Soccer')
plt.hist(socSore, bins = [1, 2, 3, 4, 5, 6], color = 'b', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Game')
plt.hist(socNot, bins = [1, 2, 3, 4, 5, 6], color = 'r', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Normal')
plt.legend()
pylab.savefig('Graphs\\8.png')

print stats.ks_2samp(socSore, socNot)
print stats.mode(socSore), stats.mode(socNot)

plt.figure()
plt.xlabel('Soreness after Game')
plt.ylabel('Frequency')
plt.title('Post-Game Soreness: Volleyball')
plt.hist(volSore, bins = [1, 2, 3, 4, 5, 6], color = 'b', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Game')
plt.hist(volNot, bins = [1, 2, 3, 4, 5, 6], color = 'r', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Normal')
plt.legend()
pylab.savefig('Graphs\\8b.png')

print stats.ks_2samp(volSore, volNot)
print stats.mode(volSore), stats.mode(volNot)
