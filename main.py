"""
    This file runs various experiments using the dataset 
    to fit and score knn, logistic regression and decision tree
    algorithms. 
    
    knn -> varies number of neighbors

    decision tree -> varies the depth of the decision tree

    logistic regression -> varies de solver and the inverse of regularization strength
"""
from subprocess import run

for i in range(1, 18, 2):
    with open(f'knn_test_data/knn_{i}.test', 'w') as file:
        run(['python', 'src/knn.py', str(i)], stdout=file)
for i in range(1, 17):
    with open(f'tree_test_data/tree_{i}.test', 'w') as file:
        run(['python', 'src/tree.py', str(i)], stdout=file)

with open(f'regression_test_data/regression_lbfgs_10.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'lbfgs', '1.0'], stdout=file)
with open(f'regression_test_data/regression_lbfgs_05.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'lbfgs', '0.5'], stdout=file)
with open(f'regression_test_data/regression_lbfgs_01.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'lbfgs', '0.1'], stdout=file)
with open(f'regression_test_data/regression_lbfgs_09.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'lbfgs', '0.9'], stdout=file)

with open(f'regression_test_data/regression_liblinear_10.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'liblinear', '1.0'], stdout=file)
with open(f'regression_test_data/regression_liblinear_05.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'liblinear', '0.5'], stdout=file)
with open(f'regression_test_data/regression_liblinear_01.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'liblinear', '0.1'], stdout=file)
with open(f'regression_test_data/regression_liblinear_09.test', 'w') as file:
        run(['python', 'src/logisticregression.py', 'liblinear', '0.9'], stdout=file)