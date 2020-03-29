
# app.py
#importando biblioteca python csv
import csv
# importando o NumPy para tratar de CSV
import numpy as np
# importando o Flask
from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args

import pandas

app = Flask(__name__)
app.debug = True

df = pandas.read_csv('./teste.csv')

X = df.iloc[:, :-1].values
y = df.iloc[:, 3].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')

# Calculates the means of columns
imputer = imputer.fit(X[:, 1:3])

# Applies those means
X[:, 1:3] = imputer.transform(X[:, 1:3])

data = df.to_dict(orient = 'records')

def get_users(offset=0, per_page=20):

    return data[offset: offset + per_page]

@app.route('/')
def index():

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    total = len(data)

    pagination_users = get_users(offset=offset, per_page=per_page)

    pagination = Pagination(page=page,
                            per_page=per_page,
                            total=total,
                            css_framework='bootstrap4')

    print(pagination_users)

    return render_template('index.html',
                           data=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)
# at the end point /
@app.route("/")
# call method hello
def hello():
    # aqui retorna "hello world"
    return "Hello World!"
# na execução de python app.py
if __name__ == "__main__":
    # execute o aplicativo Flask
    app.run(debug=True)
