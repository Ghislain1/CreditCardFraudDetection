# CreditCardFraudDetection
Data set: Data on the transaction of credit cards is used here as a data set.

# References
- https://www.youtube.com/watch?v=7eh4d6sabA0&t=1024s ==> music.csv

# Usage  requirements
py -m pip install -r requirements.txt
py  -m pip freeze > requirements.txt ==> To List package inside txt fil if you forgot to  it 

# Terminologie
- cross validation ?
- hyper-parameter tuning ??

# Workflow (Python Data Science)
- [Import Data](#import-data)
- [Clean Data](#clean-data)
- [Split the Data into Training/Test sets](#split-the-data-into-training-test-sets)
- Create a Model
- Train The Model
- Make Predictions
- Evaluate and Improve

## Import Data
- Using pandas and read_csv
- Recognize Features 

## Clean Data
- Removing duplicate
- Take care Currency ie. $

## Split the Data into Training/ Test sets
- Output  sets call y
- Input sets call X
- drop (columns=['column_name'])
- matrix ['column_name']

## Create a model
- import classifier
## Train The Model
- fit  or tain the model
## Make Predictions
- ask model to make  2 predictions at the same time ==> model.predict([[21,1], [22,0]]) 
- means which kind of music a 21th woman likes?
## Evaluate and Improve
- Split Data into test sets
- Calculate score using 


# Sklearn modules
- sklearn.tree
- sklearn.model_selection
- sklearn.ensemble
- joblib  for [model persistence](https://scikit-learn.org/stable/model_persistence.html)
- [API](https://scikit-learn.org/stable/api/sklearn.metrics.html)
- Nice structure 
