import csv
import serial
import numpy as np
from sklearn import preprocessing, svm, cross_validation
from sklearn.neighbors import KNeighborsClassifier
 
data = np.loadtxt('combineddata.csv', delimiter=',')

X = data
y = []
for i in range(50):
	y.append("left")
for j in range(50):
	y.append("right")

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=0)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print(clf.score(X_test, y_test))

neigh = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
print(neigh.score(X_test, y_test))

# Listen for a couple of seconds for the next swipe and predicts a class.
'''
total = []
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
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
print(clf.predict(n))
'''



