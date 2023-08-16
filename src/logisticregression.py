import pandas as pd
from sys import argv
import kfolds as kf
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing

df = pd.read_csv("./dataset/Phishing_Legitimate_full.csv")

y = df['CLASS_LABEL']
X = df.drop(['id','CLASS_LABEL'],axis=1) # Drops Id label
norm = preprocessing.normalize(X, axis=0, norm="max") # Normalizes by feature

classifier = LogisticRegression(max_iter=1000, tol=float(argv[2]), solver=argv[1])
with open('regression_test_data/regression_scores.log', 'a+') as log_file:
    log_file.write(argv[1] + ', ' + argv[2] + ', ' + str(kf.cross_validate(classifier, norm, list(y.values), 10, 2)).replace('[', '').replace(']', '') + '\n')