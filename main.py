"""
    This file runs various experiments using the dataset 
    to fit and score knn, logistic regression and decision tree
    algorithms. 
    
    knn -> varies number of neighbors

    decision tree -> varies the depth of the decision tree

    logistic regression -> varies de solver and the inverse of regularization strength
"""
from subprocess import run

with open('knn_test_data/knn_scores.log', 'w'), open('regression_test_data/regression_scores.log', 'w'), open('tree_test_data/tree_scores.log', 'w'):
       print('Created score files')
for i in range(1, 18, 2):
    with open(f'knn_test_data/knn_{i}.test', 'w') as file:
        run(['python', 'src/knn.py', str(i)], stdout=file)
for i in range(1, 17):
    with open(f'tree_test_data/tree_{i}.test', 'w') as file:
        run(['python', 'src/tree.py', str(i)], stdout=file)
for i in range(6):
    e = (-1*i)
    lr = 10**e
    with open(f'regression_test_data/regression_lbfgs_{i}.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'lbfgs', str(lr)], stdout=file)
    with open(f'regression_test_data/regression_liblinear_{i}.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'liblinear', str(lr)], stdout=file)

