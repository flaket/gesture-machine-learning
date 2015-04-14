import csv
import numpy as np

data1 = np.loadtxt('far-50.csv', delimiter=',')
data2 = np.loadtxt('near-50.csv', delimiter=',')
data3 = np.loadtxt('up-swipe-50.csv', delimiter=',')
data4 = np.loadtxt('up-flick-50.csv', delimiter=',')
data5 = np.loadtxt('down-swipe-50.csv', delimiter=',')
data6 = np.loadtxt('down-flick-50.csv', delimiter=',')
data7 = np.loadtxt('left-swipe-50.csv', delimiter=',')
data8 = np.loadtxt('left-flick-50.csv', delimiter=',')
data9 = np.loadtxt('right-swipe-50.csv', delimiter=',')
data10 = np.loadtxt('right-flick-50.csv', delimiter=',')

partition = 1

with open('100.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data1[:len(data1)/partition])
    a.writerows(data2[:len(data2)/partition])
    a.writerows(data3[:len(data3)/partition])
    a.writerows(data4[:len(data4)/partition])
    a.writerows(data5[:len(data5)/partition])
    a.writerows(data6[:len(data6)/partition])
    a.writerows(data7[:len(data7)/partition])
    a.writerows(data8[:len(data8)/partition])
    a.writerows(data9[:len(data9)/partition])
    a.writerows(data10[:len(data10)/partition])

