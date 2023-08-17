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

with open('tree_test_data/tree_scores.log', 'a+') as log_file:
    log_file.write(argv[1] + ', ' + str(kf.cross_validate(classifier, list(x.values), list(y.values), 10, log=2)).replace('[', '').replace(']', '') + '\n')
plt.figure()
tree.plot_tree(classifier)
plt.savefig('./tree_test_data/tree_depth_' + str(depth) + '.pdf',format="pdf",bbox_inches = "tight")