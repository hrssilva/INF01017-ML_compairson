#from pandas import DataFrame

def confusion_matrix(y_true, y_pred, labels=None):
    if not labels:
        labels = sorted(set(y_pred).union(set(y_true)))
    lookup_d = dict()
    lookup_c = 0
    matrix = [[0 for _ in range(len(labels))] for _ in range(len(labels))]
    for label in labels:
        lookup_d[label] = lookup_c
        lookup_c += 1
    print(lookup_d)
    print(matrix)
    for i in range(len(y_pred)):
        matrix[lookup_d[y_true[i]]][lookup_d[y_pred[i]]] +=1
    return matrix

def precision(conf_matrix):
    pass

def recall(conf_matrix):
    pass

def accuracy(conf_matrix):
    pass

def f1_measure(conf_matrix):
    pass