# -*- coding: utf-8 -*-
"""Crop Recommendation System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NlHflYQjI0JXtn8EumM3xe01SR-iMjZw

# Crop Recommendation System
"""

# Importing libraries

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
import time
warnings.filterwarnings('ignore')

# Reading file path
PATH = '/content/Crop_recommendation.csv'
df = pd.read_csv(PATH)

"""## Exploratory Data Analysis

First we preview the data and we look into the size, shape, columns and labels in the dataset.
"""

df.describe()

df.info()

df.head()

df.tail()

df.size

df.shape

df.columns

df['label'].unique()

df.dtypes

df['label'].value_counts()

# we use the heatmap to check for multicollinearity
sns.heatmap(df.corr(),annot=True)

#separating the features and the label
features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']
labels = df['label']

#bar plot to monitor the value of the labels against each feature
def crop_relation_visual(yfeature):
    ax = sns.set_style('whitegrid')
    plt.subplots(figsize=(15,8))

    ax = sns.barplot(x=labels, y=yfeature, data=df, ci=None,palette='rocket')
    ax.bar_label(ax.containers[0], fontsize=12)

    plt.xticks(rotation=90, fontsize=14)
    plt.yticks(rotation=0, fontsize=14)
    plt.title("Crops Relation with " + str(yfeature), fontsize = 24)
    plt.xlabel("Crops Name", fontsize = 18)
    plt.ylabel("values of " + str(yfeature), fontsize = 18)

for x in features:
    crop_relation_visual(x)

#box plot to monitor the range of the labels against each feature
def crop_boxplot_visual(yfeature):
    ax = sns.set_style('whitegrid')
    plt.subplots(figsize=(15,8))
    sns.boxplot(x=yfeature, y=labels, data=df,palette='rocket')

    plt.title("Crops Relation with " + str(yfeature), fontsize = 24)
    plt.xlabel("values of " + str(yfeature), fontsize = 18)
    plt.ylabel("Crops Name", fontsize = 18)

for x in features:
    crop_boxplot_visual(x)

"""After the data preprocessing we notice the following about the data:


*   There are no null values
*   Multicollinearity amongst the features is not high
*   There is no strong evidence of outlier presence
*   The distribution of the data is balanced for the labels

Hence, we can go forward with the modelling phase since there are no problems with the data that would require preprocessing.


"""

# Initializing empty lists to append all model's name and corresponding accuracy to monitor their performance
acc = []
model = []
tt = []

# Splitting into train and test data with 80% of the data as training data

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

"""# Model Training

We will compare the performance of various models for our given dataset to select a suitable one. Since we are performing a classification task here the models selected for this problem are:
*   Decision Tree
*Naive Bayes
*Random Forest
*Gradient Boosting

These algorithms have been selected since they are popularly used for tasks which require multiclass classification.

# Decision Tree
"""

from sklearn.tree import DecisionTreeClassifier

DecisionTree = DecisionTreeClassifier(criterion="entropy",random_state=2,max_depth=5)

start = time.time()
DecisionTree.fit(Xtrain,Ytrain)
stop = time.time()
tt.append((stop - start))

predicted_values = DecisionTree.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Decision Tree')
print("DecisionTrees's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))

from sklearn.model_selection import cross_val_score
# Cross validation score (Decision Tree)
score = cross_val_score(DecisionTree, features, target,cv=5)
score

"""# Guassian Naive Bayes"""

from sklearn.naive_bayes import GaussianNB

NaiveBayes = GaussianNB()

start = time.time()
NaiveBayes.fit(Xtrain,Ytrain)
stop = time.time()
tt.append((stop - start))

predicted_values = NaiveBayes.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Naive Bayes')
print("Naive Bayes's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

# Cross validation score (NaiveBayes)
score = cross_val_score(NaiveBayes,features,target,cv=5)
score

"""# Random Forest"""

from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
start = time.time()
RF.fit(Xtrain,Ytrain)
stop = time.time()
tt.append((stop - start))

predicted_values = RF.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('RF')
print("RF's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

# Cross validation score (Random Forest)
score = cross_val_score(RF,features,target,cv=5)
score

from sklearn.ensemble import GradientBoostingClassifier
grad = GradientBoostingClassifier()
start = time.time()
grad.fit(Xtrain,Ytrain)
stop = time.time()
tt.append((stop - start))

predicted_values = grad.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('GB')
print("GB's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

# Cross validation score (Gradient Boosting)
score = cross_val_score(grad,features,target,cv=5)
score

"""## Accuracy Comparison"""

#bar plot to compare the accuracy of all the models
plt.figure(figsize=[10,5],dpi = 100)
plt.title('Accuracy Comparison')
plt.xlabel('Accuracy')
plt.ylabel('Algorithm')
sns.barplot(x = acc,y = model,palette='rocket')

#bar plot to compare the training time of all the models
plt.figure(figsize=[10,5],dpi = 100)
plt.title('Time Comparison')
plt.xlabel('Training Time')
plt.ylabel('Algorithm')
sns.barplot(x = tt,y = model,palette='rocket')

accuracy_models = dict(zip(model, acc))
for k, v in accuracy_models.items():
    print (k, '-->', v)

"""After the comparison of the accuracy and the time we can see that the accuracy given by Gradient Boosting algorithm is higher than the other three but the training time taken by it is comparatively higher as well. Hence we can conclude that for this model choosing Naive Bayes or Random Forest as suitable model is fine since the time trade off can be justified."""