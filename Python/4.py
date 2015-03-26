import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv
import PACC

stressList = []
moodList = []
reader = PACC.getPlayerDataArray(string=1, type=0)
combo = []
for row in reader:
	tmpStress = int(row[6])
	tmpMood = int(row[7])
	stressList.append(tmpStress)
	moodList.append(tmpMood)
	combo.append([tmpStress, tmpMood])

plt.figure()
plt.scatter(moodList, stressList)
plt.xlabel('Mood')
plt.ylabel('Stress')
plt.title('Scatter of All Volleyball Players Mood vs. Stress')
pylab.savefig("Graphs/volleyBallMoodVStressScatter.png")


freq=[]
for element in combo:
	check = 0
	if len(freq) > 0:
		for thing in freq:
			if element[0] == thing[0]: 
					if element[1] == thing[1]:
						thing[2] = thing[2] + 1
						check = 1
	if check == 0:
		freq.append([element[0], element[1], 0])

xlist=[]
ylist=[]
zlist=[]

for element in freq:
	xlist.append(element[0])
	ylist.append(element[1])
	zlist.append(element[2] * 8)


plt.figure()
plt.scatter(ylist, xlist, zlist)
plt.xlabel('Mood')
plt.ylabel('Stress')
plt.title('Scatter of All Volleyball Players Mood vs. Stress')
pylab.savefig("Graphs/volleyBallMoodVStressScatter2.png")