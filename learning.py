import numpy as np
from sklearn import preprocessing, svm, cross_validation
from sklearn.neighbors import KNeighborsClassifier

X = np.loadtxt('data/f-n-us-uf-ds-df-ls-lf-rs-rf-500.csv', delimiter=',')
y = []

for i in range(50):
	y.append("far")
for i in range(50):
	y.append("near")
for i in range(50):
	y.append("up-swipe")
for i in range(50):
	y.append("up-flick")
for i in range(50):
	y.append("down-swipe")
for i in range(50):
	y.append("down-flick")
for i in range(50):
	y.append("left-swipe")
for i in range(50):
	y.append("left-flick")
for i in range(50):
	y.append("right-swipe")
for i in range(50):
	y.append("rigth-flick")

print("#Data samples: " + str(len(X)))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=0)

svc_lin = svm.LinearSVC().fit(X_train, y_train)
print("SVC-linear: " + str(svc_lin.score(X_test, y_test)))

svc = svm.SVC(C=1.0, kernel='poly').fit(X_train, y_train)
print("SVC-poly:   " + str(svc.score(X_test, y_test)))

neigh = KNeighborsClassifier(n_neighbors=3, weights='uniform').fit(X_train, y_train)
print("KNeighbors: " + str(neigh.score(X_test, y_test)))
