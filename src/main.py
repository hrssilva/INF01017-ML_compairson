import matplotlib.pyplot as plt # para visualização de informações
import pandas as pd
import kfolds as kf
from sklearn.neighbors import KNeighborsClassifier


#df = pd.read_csv("dataset/Phishing_Legitimate_full.csv")
#kf.create_folds(df, 7)
classifier = KNeighborsClassifier(1)
kf.cross_validate(classifier, [[1, 6], [2, 5], [3, 4], [4, 3], [5, 6], [6, 5]], [1, 1, 0, 0, 1, 0], 3, 2)

