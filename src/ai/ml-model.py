# Пример модели классификации
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target
model = RandomForestClassifier()
model.fit(X, y)
print("Accuracy:", model.score(X, y))