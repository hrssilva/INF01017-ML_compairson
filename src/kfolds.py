from time import time
from numpy import average, std
import metrics as met
from sklearn import preprocessing


def create_folds_sk(X, y, k):

    labels = sorted(set(y)) #Determina quantos grupos serão avaliados
    sy = sorted(enumerate(y), key=lambda a : a[1])
    quantity = []
    offsets = []
    folds = [[] for _ in range(k)]
    position = 0
    for label in labels: 
        quantity.append(y.count(label))
        offsets.append(position)
        position += quantity[-1]
    looping = True
    counting = 0
    fold_i = 0
    while looping:
        looping = False
        for i in range(len(quantity)):
            if counting < quantity[i]:
                folds[fold_i].append(sy[counting + offsets[i]][0])
                looping = True
        counting += 1
        fold_i = (fold_i + 1) % k     
    return folds

def cross_validate(classifier, X, y, k, normalize=False, log=False):
    """
        Apply k-fold cross validation to classifier, using data X and target y
            'classifier' -> The classifier to validate
            
            'X' -> The data to be used, containing all features except the target column

            'y' -> The target column to fit and score the data

            'k' -> The number of folds to be used during validation
            
            'normalize' -> If the data should be normalized
            
            'log' -> The logging degree of the validation ( 0 = no log, 1 = log results, 
            2 = log results and all iterations )
        Returns an array-like object containing the mean and standard deviation for every metric, 
        in the form: [accuracy, recall, precision, f1-measure, specificity]
    """
    folds = create_folds_sk(X, y, k)
    all_acc = []
    all_rec = []
    all_prec = []
    all_f1 = []
    all_spec = []
    labels = set(y)
    if log > 0:
        print(f'Starting cross validation with {k} folds')
    start = time()
    for i in range(k):
        train_x = []
        test_x = []
        train_y = []
        test_y = []
        for j in range(k):
            if j == i:
                for p in folds[j]:
                    test_x.append(X[p])
                    test_y.append(y[p])
            else:
                for p in folds[j]:
                    train_x.append(X[p])
                    train_y.append(y[p])
        if normalize:
            test_x = preprocessing.normalize(test_x, axis=0, norm="max") # Normalizes test
            train_x = preprocessing.normalize(train_x, axis=0, norm="max") # Normalizes test
        classifier.fit(train_x, train_y)
        pred = classifier.predict(test_x)
        cm = met.confusion_matrix(test_y, pred, labels)
        accuracy = met.accuracy(cm)
        recall = met.recall(cm)
        precision = met.precision(cm)
        f1measure = met.f1_measure(cm)
        specificity = met.specificity(cm)

        if log > 1: 
            print(f'Iteration #{i}:')
            print(f'\tConfusion matrix =')
            [print(f'\t\t{line}') for line in cm]
            print(f'\taccuracy = {accuracy}')
            print(f'\trecall = {recall}')
            print(f'\tprecision = {precision}')
            print(f'\tspecificity = {specificity}')

        all_acc.append(accuracy)
        all_rec.append(recall)
        all_prec.append(precision)
        all_f1.append(f1measure)
        all_spec.append(specificity)
    end = time()
    score_acc = [average(all_acc), std(all_acc)]
    score_rec = [average(all_rec), std(all_rec)]
    score_prec = [average(all_prec), std(all_prec)]
    score_f1 = [average(all_f1), std(all_f1)]
    score_spec = [average(all_spec), std(all_spec)]
    if log > 0:
        print('Final score:')
        print(f'\tCross validation elapsed time (seconds):')
        print(f'\t\ttime = {end - start}')
        print('\tAccuracy:')
        print(f'\t\tmean = {score_acc[0]}')
        print(f'\t\tdeviation = {score_acc[1]}')

        print('\tRecall:')
        print(f'\t\tmean = {score_rec[0]}')
        print(f'\t\tdeviation = {score_rec[1]}')

        print('\tPrecision:')
        print(f'\t\tmean = {score_prec[0]}')
        print(f'\t\tdeviation = {score_prec[1]}')

        print('\tf1-measure:')
        print(f'\t\tmean = {score_f1[0]}')
        print(f'\t\tdeviation = {score_f1[1]}')

        print('\tspecificity:')
        print(f'\t\tmean = {score_spec[0]}')
        print(f'\t\tdeviation = {score_spec[1]}')

    return [score_acc, score_rec, score_prec, score_f1, score_spec]


    

