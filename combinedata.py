import csv
import numpy as np

data1 = np.loadtxt('50-left-96data.csv', delimiter=',')
data2 = np.loadtxt('50-right-96data.csv', delimiter=',')
#data3 = np.loadtxt('leftdata.csv', delimiter=',')
#data4 = np.loadtxt('rightdata.csv', delimiter=',')

#print(len(data1))

with open('combined-50-lr-96data.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data1)
    a.writerows(data2)
   # a.writerows(data3)
   # a.writerows(data4)

