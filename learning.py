import numpy as np
import random as r
from sklearn import preprocessing, svm, cross_validation
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

X = np.loadtxt('data/500.csv', delimiter=',')
X = preprocessing.scale(X)
y = []
samples_per_label = 50
loops = 10


def create_labels():
    for i in range(samples_per_label):
        y.append("far")
    for i in range(samples_per_label):
        y.append("near")
    for i in range(samples_per_label):
        y.append("up-swipe")
    for i in range(samples_per_label):
        y.append("up-flick")
    for i in range(samples_per_label):
        y.append("down-swipe")
    for i in range(samples_per_label):
        y.append("down-flick")
    for i in range(samples_per_label):
        y.append("left-swipe")
    for i in range(samples_per_label):
        y.append("left-flick")
    for i in range(samples_per_label):
        y.append("right-swipe")
    for i in range(samples_per_label):
        y.append("rigth-flick")


def classify():
    if len(X) == len(y):
        results = []
        svc_lin_score = 0
        svc_score = 0
        kNeighbors_score = 0
        randomForest_score = 0
        gradientBoosting_score = 0
        extraTrees_score = 0
        bagging_score = 0
        decisionTree_score = 0
        logisticRegression_score = 0

        for i in range(loops):
            seed = r.randint(0, len(X))
            X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=seed)

            svc_lin = svm.LinearSVC().fit(X_train, y_train)
            svc_lin_score = svc_lin_score + svc_lin.score(X_test, y_test)

            svc = svm.SVC(kernel='linear').fit(X_train, y_train)
            svc_score = svc_score + svc.score(X_test, y_test)

            logisticRegression = LogisticRegression().fit(X_train, y_train)
            logisticRegression_score = logisticRegression_score + logisticRegression.score(X_test, y_test)

            '''
            kNeighbors = KNeighborsClassifier().fit(X_train, y_train)
            kNeighbors_score = kNeighbors_score + kNeighbors.score(X_test, y_test)
            decisionTree = DecisionTreeClassifier().fit(X_train, y_train)
            decisionTree_score = decisionTree_score + decisionTree.score(X_test, y_test)
            randomForest = RandomForestClassifier().fit(X_train, y_train)
            randomForest_score = randomForest_score + randomForest.score(X_test, y_test)
            extraTrees = ExtraTreesClassifier().fit(X_train, y_train)
            extraTrees_score = extraTrees_score + extraTrees.score(X_test, y_test)
            gradientBoosting = GradientBoostingClassifier().fit(X_train, y_train)
            gradientBoosting_score = gradientBoosting_score + gradientBoosting.score(X_test, y_test)
            bagging = BaggingClassifier().fit(X_train, y_train)
            bagging_score = bagging_score + bagging.score(X_test, y_test)
            '''

        results.append([str(svc_lin_score / loops), "Linear-SVC"])
        results.append([str(svc_score / loops), "SVC"])
        results.append([str(logisticRegression_score / loops), "LogisticRegression"])
        '''
        results.append([str(kNeighbors_score / loops), "KNeighbors"])
        results.append([str(decisionTree_score / loops), "DecisionTree"])
        results.append([str(randomForest_score / loops), "RandomForest"])
        results.append([str(extraTrees_score / loops), "ExtraTrees"])
        results.append([str(bagging_score / loops), "Bagging"])
        results.append([str(gradientBoosting_score / loops), "GradientBoosting"])
        '''
        results.sort(reverse=True)
        return results
    return "Mismatch in #data samples in data set X and #labels in y"

if __name__ == '__main__':
    create_labels()
    print(classify())