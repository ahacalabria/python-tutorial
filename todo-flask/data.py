#importando biblioteca python csv
import csv
# importando o NumPy para tratar de CSV
import numpy as np
# importando o Flask
from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args

import pandas

# Visual libraries
from plotly.offline import plot

import plotly.graph_objs as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

app = Flask(__name__)
app.debug = True

# df = pandas.read_csv('./teste.csv')

# X = df.iloc[:, :-1].values
# y = df.iloc[:, 3].values

# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')

# Calculates the means of columns
# imputer = imputer.fit(X[:, 1:3])

# Applies those means
# X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical data
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# Encoding the Independent Variable
# onehotencoder_X = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0])], remainder='passthrough')
# X = onehotencoder_X.fit_transform(X)

# Encoding the Dependent Variable
# onehotencoder_y = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0])], remainder='passthrough')
# y = onehotencoder_y.fit_transform(np.array([y]).T)

# Training and Test set
from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Standardize features by removing the mean and scaling to unit variance
# from sklearn.preprocessing import StandardScaler

# Scaling the Independent Variable
# Is it necessary rescale dummy variables? To keep the mean, no. To let all at similar range, yes
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

# Scaling the Dependent Variable
# If is a classifier, it is not necessary
# sc_y = StandardScaler()
# y_train = sc_y.fit_transform(y_train)

# Dataset
dataset = pandas.read_csv('teste.csv')

# Heatmap of correlation matrix
# corr = dataset.corr()
# data = [go.Heatmap( z=corr.corr().values, x=list(corr.columns), y=list(corr.index), colorscale='Viridis')]
# plot(data, filename='pandas-heatmap')

sns.set(style="ticks")
# col =  ['SalePrice', 'OverallQual']#, 'GrLivArea', 'GarageCars','GarageArea' ,
        #'TotalBsmtSF', 'FullBath', 'YearBuilt','TotRmsAbvGrd']
col = ['Age','Salary']
sns.pairplot(dataset[col])

figure = ff.create_scatterplotmatrix(dataset[col],diag='histogram', width=1200, height=1200)
plot(figure, filename='pandas-scatter')