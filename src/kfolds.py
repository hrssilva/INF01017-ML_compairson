import matplotlib.pyplot as plt # para visualização de informações
import pandas as pd

def create_folds(df, k):

    labels = df["CLASS_LABEL"].unique() #Determina quantos grupos serão avaliados
    grouped = df.groupby(df["CLASS_LABEL"]) #Separa os grupos em presentes em "CLASS_LABEL"
    df_grouped_rand = [None] * len(labels)
    prop = [None] * len(labels)

    for i in range(len(labels)):
        df_grouped_rand[i] = grouped.get_group(labels[i]).sample(frac = 1)
        prop[i] = len(df_grouped_rand[i])/len(df)

    elements_in_fold = int(len(df)/k)
   
    fold =[[0 for x in range(k)] for y in range(elements_in_fold)]
    print(fold)
    for i in range(0 , len(labels)): # TODO FINISH KFOLD 
        prop[i] * len(df)


    