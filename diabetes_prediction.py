# -*- coding: utf-8 -*-
"""diabetes_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YHK_g3S0KK87CDe6ygvfy40AAtMao8IB
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# %matplotlib inline
import sklearn as sk
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("/content/diabetes.csv")

data.shape

data.head()

data.isnull().values.any()

import seaborn as sns
import matplotlib.pyplot as plt
corrnat = data.corr()
top_corr_features = corrnat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")

data.corr()

diabetes_map = {True: 1, False: 0}

data["Pregnancies"] = data["Glucose"].map(diabetes_map)

data.head(5)

diabetes_true_count = len(data.loc[data['BloodPressure'] == True])
diabetes_false_count = len(data.loc[data['BloodPressure'] == False])

(diabetes_true_count,diabetes_false_count)

data = data.fillna(0)

data.fillna(0, inplace=True)

data.dtypes

from sklearn.model_selection import train_test_split
feature_columns = ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"]
predicted_class = ['DiabetesPedigreeFunction']

X = data[feature_columns].values
y = data[predicted_class].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state=10)

print("total number of rows : {0}".format(len(data)))
print("number of rows missing Pregnancies: {0}".format(len(data.loc[data['Pregnancies'] == 0])))
print("number of rows missing Glucose: {0}".format(len(data.loc[data['Glucose'] == 0])))
print("number of rows missing BloodPressure: {0}".format(len(data.loc[data['BloodPressure'] == 0])))
print("number of rows missing SkinThickness: {0}".format(len(data.loc[data['SkinThickness'] == 0])))
print("number of rows missing Insulin: {0}".format(len(data.loc[data['Insulin'] == 0])))
print("number of rows missing BMI: {0}".format(len(data.loc[data['BMI'] == 0])))
print("number of rows missing DiabetesPedigreeFunction: {0}".format(len(data.loc[data['DiabetesPedigreeFunction'] == 0])))
print("number of rows missing Age: {0}".format(len(data.loc[data['Age'] == 0])))
print("number of rows missing Outcome: {0}".format(len(data.loc[data['Outcome'] == 0])))

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=0, strategy='constant')


X_train = imputer.fit_transform(X_train)
X_test = imputer.fit_transform(X_test)

from scipy import stats
import numpy as np
f=open('/content/diabetes.csv','r').readlines()
w=f[1].split()
l1=w[1:8]
l2=w[8:15]
list1=[float(x) for x in l1]
list1
l3=w[1:8]
l4=w[8:15]
list2=[float(y) for x in l3]
list2

from sklearn.model_selection import RandomizedSearchCV
import xgboost

classifier=xgboost.XGBClassifier(X,y)

params={
 "learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ]

}

random_search=RandomizedSearchCV(classifier,param_distributions=params,n_iter=5,scoring='roc_auc',n_jobs=-1,cv=5,verbose=3)

def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))

from datetime import datetime
start_time = timer(None)

timer(start_time)

random_search

classifier=xgboost.XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
       colsample_bytree=0.3, gamma=0.0, learning_rate=0.25,
       max_delta_step=0, max_depth=3, min_child_weight=7, missing=None,
       n_estimators=100, n_jobs=1, nthread=None,
       objective='binary:logistic', random_state=0, reg_alpha=0,
       reg_lambda=1, scale_pos_weight=1, seed=None, silent=True,
       subsample=1)

from sklearn.model_selection import cross_val_predict

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

data.groupby('Outcome').mean()

data['Outcome'].value_counts()

print(X)

print(Y)

X = data.drop(columns = 'Outcome', axis=1)
Y = data['Outcome']

X = standardized_data
Y = data['Outcome']

X = standardized_data
Y = data['Outcome']

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, Y_train)

X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)

input_data = (8,187,92,29,177,35.8,0.876,81,151)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')