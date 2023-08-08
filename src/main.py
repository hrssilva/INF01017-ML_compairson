import matplotlib.pyplot as plt # para visualização de informações
import pandas as pd
import kfolds as kf


#df = pd.read_csv("dataset/Phishing_Legitimate_full.csv")
#kf.create_folds(df, 7)
folds = kf.create_folds_sk([1, 2, 3, 4], [0, 1, 1, 0], 2)
print(folds)
