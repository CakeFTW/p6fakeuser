#Importing stuff
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn.svm as clf 
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.utils.multiclass import unique_labels
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, classification_report
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from time import time
import pickle
from sklearn.externals import joblib
import dataprocess as dp 

#Read the data and labels csv files and save them to a DataFrame
df_data = pd.read_csv("ep_noflip_data.csv")
df_labels = pd.read_csv("ep_noflip_labels.csv")
#print(df_data.head())

#1-Hot-Encode the labels
df_labels['0'] = df_labels['0'].astype(str) #Turns int into str
df_labels = pd.get_dummies(df_labels) #1-hot-encode the categories
#print(df_labels.head())
print("OG shape:", df_data.shape)

for i, col in enumerate(df_labels.columns.tolist(), 1):
    df_labels.loc[:, col] *= i
df_labels = df_labels.sum(axis=1)
df_data = dp.circle_scale(df_data.values)

#Create VarianceThreshold object with a variance with a threshold of 0.5
#thresholder = VarianceThreshold(threshold=.5)
#df_data = thresholder.fit_transform(df_data)

#Scale the data
#scaler = MinMaxScaler()
#df_data = scaler.fit_transform(df_data)

#Dimensionality reduction, keeping 95% of the variance
#pca = PCA(.95)
#df_data_projected = pca.fit_transform(df_data)
#print("Number of dimensions:",pca.n_components_)
#print("Projected shape:", df_data_projected.shape)

#Split the date and labels
X_train, X_test, y_train, y_test = train_test_split(df_data, df_labels, test_size=0.2, random_state=420)
print('ya')

#Make the models
logistic = LogisticRegression(random_state=420, multi_class='ovr', max_iter=1000)
C = [0.0001, 0.001, 0.01, 1, 100]
solver = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
hyperparameters = dict(C=C, solver=solver)
clf = GridSearchCV(logistic, hyperparameters, cv=5, verbose=0)

#Train the model
start = time()
clf.fit(X_train, y_train)
print('yeet with a time of:', time() - start, 'seconds')
print('Best Parameters',clf.best_params_)

#Testing the model
y_pred = clf.predict(X_test)
#y_pred_prob = clf.predict_proba(X_test)
#print(y_pred_prob)

#Evaluation
labels = ['nothing','forward','up','back','left','down','right']
print("Accuracy Score:", accuracy_score(y_test, y_pred))
# print("AUC Score:", roc_auc_score(y_test, y_pred))
# print(classification_report(y_test,y_pred, target_names=labels))
# cm = confusion_matrix(y_test.values.argmax(axis=1), y_pred.argmax(axis=1))
# print(cm)

# #Saveing the model
pkl_filename = "lr.pkl"  
with open(pkl_filename, 'wb') as file:  
    pickle.dump(clf, file)
print('Model saved')