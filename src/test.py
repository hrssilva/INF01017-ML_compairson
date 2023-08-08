from sklearn import datasets
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression

X, y = datasets.load_diabetes(return_X_y=True)
print(X)
print(y)
z =datasets.load_diabetes()
print(z)