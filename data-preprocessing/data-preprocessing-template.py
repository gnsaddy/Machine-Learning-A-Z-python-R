#  data preprocessing

from sklearn.preprocessing import Imputer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# load csv file
dataSet = pd.read_csv("./Data.csv")
# matrix for independent variables X
X = dataSet.iloc[:, :-1].values
# dependent variables vector
Y = dataSet.iloc[:, 3]


# taking care of missing data
# from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
# fit the matrix which having missing data
imputer = imputer.fit(X[:, 1:])
X[:,1:]=imputer.transform(X[:,1:])
X
dataSet.head(10)
