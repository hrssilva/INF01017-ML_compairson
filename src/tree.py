import pandas as pd
import kfolds as kf
from sklearn import tree
import matplotlib.pyplot as plt
from sys import argv

depth = int(argv[1])
df = pd.read_csv("./dataset/Phishing_Legitimate_full.csv")

y = df['CLASS_LABEL']
x = df.drop(['id','CLASS_LABEL'],axis=1) # Drops Id label

classifier = tree.DecisionTreeClassifier(max_depth=depth)
classifier.fit(x,y)


kf.cross_validate(classifier, list(x.values), list(y.values), 10, 1)
plt.figure()
tree.plot_tree(classifier)
plt.savefig('./tree_test_data/tree_depth_' + str(depth) + '.pdf',format="pdf",bbox_inches = "tight")