import csv
import numpy as np

data1 = np.loadtxt('2finger-swipe-left-50.csv', delimiter=',')
data2 = np.loadtxt('2finger-swipe-rigth-50.csv', delimiter=',')
data3 = np.loadtxt('2finger-flick-left-50.csv', delimiter=',')
data4 = np.loadtxt('2finger-flick-rigth-50.csv', delimiter=',')

#print(len(data1))
#print(len(data2))
#print(len(data3))
#print(len(data4))

with open('combined-2finger-sf-lr-50.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data1)
    a.writerows(data2)
    a.writerows(data3)
    a.writerows(data4)
