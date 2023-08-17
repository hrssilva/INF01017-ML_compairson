from sys import argv
import pandas as pd
import kfolds as kf
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing


df = pd.read_csv("./dataset/Phishing_Legitimate_full.csv")

y = df['CLASS_LABEL']
x = df.drop(['id','CLASS_LABEL'],axis=1) # Drops Id label

classifier = KNeighborsClassifier(int(argv[1]))

with open('knn_test_data/knn_scores.log', 'a+') as log_file:
    log_file.write(argv[1] + ', ' + str(kf.cross_validate(classifier, list(x.values), list(y.values), 10, normalize=True, log=2)).replace('[', '').replace(']', '') + '\n')

