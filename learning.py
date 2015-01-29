import csv
import serial
import numpy as np
from sklearn import preprocessing, svm, cross_validation
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans 

X = np.loadtxt('combined-2finger-sf-lr-50.csv', delimiter=',')
y = []

for i in range(50):
	y.append("swipe-left")
for i in range(50):
	y.append("swipe-rigth")
for i in range(50):
	y.append("flick-left")
for i in range(50):
	y.append("flick-rigth")

print("#Data samples: " + str(len(X)))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=0)

svc_lin = svm.LinearSVC().fit(X_train, y_train)
print("SVC-linear: " + str(svc_lin.score(X_test, y_test)))

svc = svm.SVC(C=1.0, kernel='poly').fit(X_train, y_train)
print("SVC-poly:   " + str(svc.score(X_test, y_test)))

neigh = KNeighborsClassifier(n_neighbors=2, weights='uniform', p=10).fit(X_train, y_train)
print("KNeighbors: " + str(neigh.score(X_test, y_test)))
