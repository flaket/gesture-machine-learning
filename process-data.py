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

for i in range(1,51):
	total = []
	try:
		print("Listening for swipe for 2 seconds..")
		for line in ser:
			line = line.decode()
			line = line.split(' ')
			del line[-1]
			values = list(map(int, line))
			total = total + values
	except serial.SerialException:
		print('caught SerialException!')
	sensor1 = []
	sensor2 = []
	sensor3 = []
	sensor4 = []
	for j in range(0, len(total), 4):
		sensor1.append(total[j+0])
		sensor2.append(total[j+1])
		sensor3.append(total[j+2])
		sensor4.append(total[j+3])
	sensor3.extend(sensor4)
	sensor2.extend(sensor3)
	sensor1.extend(sensor2)
	if len(sensor1) > 0:
		result = hist(sensor1)
		data.append(result)
		print("Stored result: " + str(i))

with open('2finger-swipe-up-50.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data)

#plt.bar(np.arange(128), tuple(result))
#plt.show()


