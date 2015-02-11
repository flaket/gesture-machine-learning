import numpy as np
import random as r
from sklearn import preprocessing, svm, cross_validation
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier, NearestCentroid
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier, BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

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

if len(X) == len(y):
  seed = r.randint(0, len(X))
  X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=seed)
  results = []

  svc_lin = svm.LinearSVC().fit(X_train, y_train)
  results.append([str(svc_lin.score(X_test, y_test)), "Linear-SVC"])

  svc = svm.SVC().fit(X_train, y_train)
  results.append([str(svc.score(X_test, y_test)), "SVC"])

  kNeighbors = KNeighborsClassifier().fit(X_train, y_train)
  results.append([str(kNeighbors.score(X_test, y_test)), "KNeighbors"])

  nearestCentroid = NearestCentroid().fit(X_train, y_train)
  results.append([str(nearestCentroid.score(X_test, y_test)), "NearestCentroid"])

  gaussianNB = GaussianNB().fit(X_train, y_train)
  results.append([str(gaussianNB.score(X_test, y_test)), "GaussianNB"])

  bernoulliNB = BernoulliNB().fit(X_train, y_train)
  results.append([str(bernoulliNB.score(X_test, y_test)), "BernoulliNB"])

  multinomialNB = MultinomialNB().fit(X_train, y_train)
  results.append([str(multinomialNB.score(X_test, y_test)), "MultinomialNB"])

  randomForest = RandomForestClassifier().fit(X_train, y_train)
  results.append([str(randomForest.score(X_test, y_test)), "RandomForest"])

  gradiantBoosting = GradientBoostingClassifier().fit(X_train, y_train)
  results.append([str(gradiantBoosting.score(X_test, y_test)), "GradientBoosting"])

  extraTrees = ExtraTreesClassifier().fit(X_train, y_train)
  results.append([str(extraTrees.score(X_test, y_test)), "ExtraTrees"])

  bagging = BaggingClassifier().fit(X_train, y_train)
  results.append([str(bagging.score(X_test, y_test)), "Bagging"])

  adaBoost = AdaBoostClassifier().fit(X_train, y_train)
  results.append([str(adaBoost.score(X_test, y_test)), "AdaBoost"])

  decisionTree = DecisionTreeClassifier().fit(X_train, y_train)
  results.append([str(decisionTree.score(X_test, y_test)), "DecisionTree"])

  results.sort(reverse=True)
  print(results)
