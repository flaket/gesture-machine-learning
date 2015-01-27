import serial
import csv
import numpy as np
from sklearn import preprocessing, svm
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
data = []

def hist(data, n=128, m=255):
	'''
	Partitions an input array of data into an n-sized array with normalized values with regard to m.
	If the input data is of a shorter length than n the returned array will be sparse.
	A larger input array will produce a denser result.
	'''
	l = len(data)
	histogram = [0] * n
	samples = int(l / n)
	if samples == 0:
		samples = int(1 / (l / n))
		for i, x in enumerate(data):
			histogram[i*samples] = x/m
	else:
		for i in range(0,n):
			histogram[i] = sum(data[i*samples:(i+1)*samples])/(m*samples)
	return histogram

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
		for i in range(0, len(total), 4):
			sensor1.append(total[i+0])
			sensor2.append(total[i+1])
			sensor3.append(total[i+2])
			sensor4.append(total[i+3])
	except serial.SerialException:
		print('caught serial-exception')
	sensor3.extend(sensor4)
	sensor2.extend(sensor3)
	sensor1.extend(sensor2)
	print(sensor1)
	#data.append(n)
	#print(data)
	result = hist(sensor1)
	print(result)
	print(len(result))
	print(sum(result))
'''
with open('s50-left-96data.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data)
'''

#n, bins = np.histogram(total, bins=96, density=True)

#width = 0.8 * (bins[1] - bins[0])
#center = (bins[:-1] + bins[1:]) / 2
plt.bar(np.arange(128), tuple(result))
plt.show()


