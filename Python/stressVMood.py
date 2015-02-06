import numpy as np
import matplotlib.pyplot as plt
import datetime
import pylab
import csv

stressList = []
moodList = []
with open('C:\\Users\\neil.xu\\Documents\\GitHub\\PACC2015\\welcome\\player_data_volleyball.csv', 'rb') as soccerFile:
	reader = csv.reader(soccerFile, delimiter=',')
	for row in reader:
		try:
			tmpStress = int(row[6])
			tmpMood = int(row[7])
			stressList.append(tmpStress)
			moodList.append(tmpMood)
		except:
			next
plt.figure()
plt.scatter(moodList, stressList)
plt.xlabel('Mood')
plt.ylabel('Stress')
plt.title('Scatter of All Volleyball Players Mood vs. Stress')
pylab.savefig("volleyBallMoodVStressScatter.png")

strMoodDict = {}

for i in range(0, len(moodList) - 1):
	if moodList[i] in strMoodDict:
		strMoodDict[moodList[i]].append(stressList[i])
	else:
		strMoodDict[moodList[i]] = []

xmood = []
ystress = []
yerror = []
for k, v in strMoodDict.items():
	print k, v
	xmood.append(k)
	sum = 0
	for element in v:
		sum += element
	sum /= len(v)
	yerror.append(np.std(v))
	ystress.append(sum)

plt.figure()
plt.scatter(xmood, ystress)
plt.errorbar(xmood, ystress, yerr = yerror)
plt.xlabel('Mood')
plt.ylabel('Stress')
plt.title('Scatter of Mood vs. Average Stress')
pylab.savefig("averageScatter.png")