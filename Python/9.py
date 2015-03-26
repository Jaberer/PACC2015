import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import PACC
from scipy import stats

socAfterGameDay = []
for x in PACC.getPlayerDataArray(string = 0, type = 1):
	try:
		socAfterGameDay.append([datetime.datetime.strptime(x[1], '%m/%d/%Y') + datetime.timedelta(days = 1), x[6]])
	except:
		pass
soc = []
for element in PACC.getPlayerDataArray(string = 0, type = 0):
	try:
		date = datetime.datetime.strptime(element[2], '%m/%d/%Y')
	except:
		pass
	for component in socAfterGameDay:
		if date in component:
			soc.append([int(element[7]), component[1]])
		else:
			soc.append([int(element[7]), 'N'])

volAfterGameDay = []
for x in PACC.getPlayerDataArray(string = 1, type = 1):
	try:
		volAfterGameDay.append([datetime.datetime.strptime(x[1], '%m/%d/%Y') + datetime.timedelta(days = 1), x[6]])
	except:
		pass
vol = []
for element in PACC.getPlayerDataArray(string = 1, type = 0):
	try:
		date = datetime.datetime.strptime(element[2], '%m/%d/%Y')
	except:
		pass
	for component in volAfterGameDay:
		if date in component:
			vol.append([int(element[7]), component[1]])
		else:
			vol.append([int(element[7]), 'N'])

wins = []
ties = []
losses = []
normal = []
for element in soc:
	if element[1] == 'W':
		wins.append(element[0])
	elif element[1] == 'L':
		losses.append(element[0])
	elif element[1] == 'T':
		ties.append(element[0])
	else:
		normal.append(element[0])
for element in vol:
	if element[1] == 'W':
		wins.append(element[0])
	elif element[1] == 'L':
		losses.append(element[0])
	elif element[1] == 'T':
		ties.append(element[0])
	else:
		normal.append(element[0])
plt.figure()
plt.xlabel('Mood')
plt.ylabel('Frequency')
plt.title('Post-Game Mood vs. Normal Mood')
plt.hist(wins + ties + losses, bins = 5, color = 'b', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Gameday')
plt.hist(normal, bins = 5, color = 'r', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Normal Day')
plt.xticks(np.arange(1, 6, 1.0))
plt.legend(bbox_to_anchor=(0.45, 0.9), bbox_transform=plt.gcf().transFigure)
pylab.savefig('Graphs\\9.png')

print "Averages"
print stats.mode(wins + ties + losses), stats.mode(normal)
print stats.ks_2samp(wins + ties + losses, normal)

plt.figure()
plt.xlabel('Mood')
plt.ylabel('Frequency')
plt.title('Post-Game Mood of Wins, Losses, and Ties')
plt.hist(wins, bins = 5, color = 'g', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Wins')
plt.hist(losses, bins = 5, color = 'c', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Losses')
plt.hist(ties, bins = 5, color = 'y', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Ties')
plt.xticks(np.arange(1, 6, 1.0))
plt.legend(bbox_to_anchor=(0.45, 0.9), bbox_transform=plt.gcf().transFigure)
pylab.savefig('Graphs\\9-0.png')

print "Averages"
print stats.mode(wins), stats.mode(losses), stats.mode(ties)
print stats.ks_2samp(wins, losses)
print stats.ks_2samp(wins, ties)
print stats.ks_2samp(ties, losses)



plt.figure()
plt.xlabel('Mood')
plt.ylabel('Frequency')
plt.title('Mood Situations')
plt.hist(wins + ties + losses, bins = 5, color = 'b', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Gameday')
plt.hist(normal, bins = 5, color = 'r', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'Normal Day')
plt.hist(wins, bins = 5, color = 'g', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Wins')
plt.hist(losses, bins = 5, color = 'c', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Losses')
plt.hist(ties, bins = 5, color = 'y', histtype = 'stepfilled', normed = True, alpha = 0.5, label = 'After Ties')
plt.xticks(np.arange(1, 6, 1.0))
plt.legend(bbox_to_anchor=(0.45, 0.9), bbox_transform=plt.gcf().transFigure)
pylab.savefig('Graphs\\9-1.png')