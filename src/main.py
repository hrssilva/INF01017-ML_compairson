import matplotlib.pyplot as plt # para visualização de informações
import pandas as pd
import kfolds as kf


df = pd.read_csv("dataset/Phishing_Legitimate_full.csv")
kf.create_folds(df, 7)
