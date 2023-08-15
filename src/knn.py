import matplotlib.pyplot as plt # para visualização de informações
import pandas as pd
import kfolds as kf
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

#df = pd.read_csv("dataset/Phishing_Legitimate_full.csv")
#kf.create_folds(df, 7)

df = pd.read_csv("./dataset/Phishing_Legitimate_full.csv")

y = df['CLASS_LABEL']
x = df.drop(['id','CLASS_LABEL'],axis=1) # Drops Id label
norm = preprocessing.normalize(x, axis=0, norm="max") # Normalizes by feature

classifier = KNeighborsClassifier(5)

kf.cross_validate(classifier, norm, list(y.values), 10, 2)

