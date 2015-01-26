import csv
import serial
import numpy as np
from sklearn import preprocessing, svm, cross_validation
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans 

X = np.loadtxt('data/combined-50-lr-96data.csv', delimiter=',')
y = []

'''
for i in range(50):
	y.append("up")
for i in range(50):
	y.append("down")
'''
for i in range(50):
	y.append("left")
for i in range(50):
	y.append("right")

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=0)

svc_lin = svm.LinearSVC().fit(X_train, y_train)
print(svc_lin.score(X_test, y_test))

svc = svm.SVC(C=0.5, kernel='poly').fit(X_train, y_train)
print(svc.score(X_test, y_test))

neigh = KNeighborsClassifier(n_neighbors=6, weights='uniform', p=5).fit(X_train, y_train)
print(neigh.score(X_test, y_test))

#kmeans = KMeans(4).fit_predict(X_train)
#print(kmeans)

# Listen for a couple of seconds for the next swipe and predicts a class.
'''
total = []
ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=2)
try:
    print("Listening for swipe for 2 seconds..")
    for line in ser:
        line = line.decode()
        line = line.split(' ')
        del line[-1]
        values = list(map(int, line))
        total = total + values
        n, bins = np.histogram(total, bins=32, density=True)
except serial.SerialException:
	print('caught serial-exception')
print(neigh.predict(n))
'''
