#  data preprocessing

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
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
print(X)
dataSet.head(10)

# Encoding categorical data
labelencoder_X = LabelEncoder() # LabelEncoder object 
labelencoder_X.fit_transform(X[:,0])
X[:,0] = labelencoder_X.fit_transform(X[:,0])
print(X)

# creating dummy variable using OneHotEncoder class
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
print(X)


# purchased column y
labelencoder_Y = LabelEncoder() # LabelEncoder object 
labelencoder_Y.fit_transform(Y)
Y = labelencoder_Y.fit_transform(Y)
print(Y)
