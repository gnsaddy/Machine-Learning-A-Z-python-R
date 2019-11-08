#  data preprocessing

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# load csv file
dataSet = pd.read_csv("./data-preprocessing/Data.csv")

print(dataSet)
dataSet.columns = ['Country', 'Age', 'Salary', 'Purchased']
print(dataSet.columns)
# matrix for independent variables X
X = dataSet.iloc[:, :-1].values
# dependent variables vector
Y = dataSet.iloc[:, 3]


# taking care of missing data
# from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
# fit the matrix which having missing data
imputer = imputer.fit(X[:, 1:])
X[:, 1:] = imputer.transform(X[:, 1:])
print(X)
dataSet.head(10)

# Encoding categorical data
labelencoder_X = LabelEncoder()  # LabelEncoder object
labelencoder_X.fit_transform(X[:, 0])
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
print(X)

# creating dummy variable using OneHotEncoder class
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
print(X)


# purchased column y
labelencoder_Y = LabelEncoder()  # LabelEncoder object
labelencoder_Y.fit_transform(Y)
Y = labelencoder_Y.fit_transform(Y)
print(Y)

# dataset splitting into train and test set
# cross validation library
# from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0
)
# feature scaling
# from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
