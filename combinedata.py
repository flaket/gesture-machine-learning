import csv
import numpy as np

leftdata = np.loadtxt('leftdata.csv', delimiter=',')
rightdata = np.loadtxt('rightdata.csv', delimiter=',')

with open('combineddata.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(leftdata)
    a.writerows(rightdata)
