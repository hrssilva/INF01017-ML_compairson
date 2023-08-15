import matplotlib.pyplot as plt # para visualização de informações
from sys import argv
import pandas as pd
import kfolds as kf
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing


df = pd.read_csv("./dataset/Phishing_Legitimate_full.csv")

y = df['CLASS_LABEL']
x = df.drop(['id','CLASS_LABEL'],axis=1) # Drops Id label
norm = preprocessing.normalize(x, axis=0, norm="max") # Normalizes by feature

classifier = KNeighborsClassifier(int(argv[1]))

kf.cross_validate(classifier, norm, list(y.values), 10, 2)

