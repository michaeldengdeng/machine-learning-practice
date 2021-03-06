from sklearn import datasets
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

score = cross_val_score(estimator=KNeighborsClassifier(), X=iris.data, y=iris.target, cv=KFold(n_splits=10))

print(score.mean())
print(score.std())
