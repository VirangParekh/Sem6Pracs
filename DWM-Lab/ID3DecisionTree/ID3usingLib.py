import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np

dataset = pd.read_csv('zoo.csv', names=['animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airbone', 'aquatic',
                                        'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'class', ])
dataset = dataset.drop(columns=['animal_name'], axis=1)

train_features = dataset.iloc[:80, :-1]
test_features = dataset.iloc[80:, :-1]
train_targets = dataset.iloc[:80, -1]
test_targets = dataset.iloc[80:, -1]
tree = DecisionTreeClassifier(criterion='entropy').fit(
    train_features, train_targets)
prediction = tree.predict(test_features)
print("The prediction accuracy is: ", tree.score(
    test_features, test_targets)*100, "%")
