#!/usr/bin/env

from sklearn import tree

# 1 for dragon
# 0 for human  
labels = [1,0,1,0,1,0,1,0]

# 1 for heavy
# 0 for lightweight
# the numbers represnt skills/xP whatever ...
features = [[1500,1],[600,0],[1270,1],[200,0],[5000,1],[500,0],[2567,1],[900,1]]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[2700,1]])
