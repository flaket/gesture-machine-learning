import serial
import csv
import numpy as np
from sklearn import preprocessing, svm
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

data = []
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
		n, bins = np.histogram(total, bins=32, density=True)
		data.append(n)
		print("Saved data sample: " + str(i))
	except serial.SerialException:
		print('caught serial-exception')

with open('rightdata.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data)

#print(data)
#n, bins = np.histogram(data, bins=32, density=True)
#print(data)

#mu, sigma = 100, 15
#x = mu + sigma * np.random.randn(10000)
#width = 0.8 * (bins[1] - bins[0])
#center = (bins[:-1] + bins[1:]) / 2
#plt.bar(center, n, align='center', width=width)
#plt.show()



