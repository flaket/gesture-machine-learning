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


#print(len(data1))
#print(len(data2))
#print(len(data3))
#print(len(data4))

with open('f-n-us-uf-ds-df-ls-lf-us-uf-500.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data1)
    a.writerows(data2)
    a.writerows(data3)
    a.writerows(data4)
    a.writerows(data5)
    a.writerows(data6)
    a.writerows(data7)
    a.writerows(data8)
    a.writerows(data9)
    a.writerows(data10)

