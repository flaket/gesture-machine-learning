import serial
import csv
import numpy as np
from sklearn import preprocessing, svm
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=2)

data = []
for i in range(1,2):
	total = []
	sensor1 = []
	sensor2 = []
	sensor3 = []
	sensor4 = []
	try:
		print("Listening for swipe for 2 seconds..")
		for line in ser:
			line = line.decode()
			line = line.split(' ')
			del line[-1]
			values = list(map(int, line))
			total = total + values
		print(total)
		for i,x in enumerate(total):
			if i==0 or (i % 4 == 0):
				sensor1.append(x)
			elif i==1 or (i % 3 == 0):
				sensor2.append(x)
			elif i==2 or (i % 2 == 0):
				sensor3.append(x)
			else: sensor4.append(x)
		print(sensor1)
		print(sensor2)
		print(sensor3)
		print(sensor4)
		print(len(total)==len(sensor1)+len(sensor2)+len(sensor3)+len(sensor4))
		#n, bins = np.histogram(total, bins=96, density=True)
		#data.append(n)
		print("Saved data sample: " + str(i))
	except serial.SerialException:
		print('caught serial-exception')
'''
with open('s50-left-96data.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data)
'''

#print(data)
#n, bins = np.histogram(data, bins=32, density=True)
#print(data)

#mu, sigma = 100, 15
#x = mu + sigma * np.random.randn(10000)
#width = 0.8 * (bins[1] - bins[0])
#center = (bins[:-1] + bins[1:]) / 2
#plt.bar(center, n, align='center', width=width)
#plt.show()



