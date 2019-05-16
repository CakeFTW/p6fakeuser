#Importing stuff
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.svm as clf 
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from time import time
import pickle
from sklearn.externals import joblib
import dataprocess as dp 

#Read the data and labels csv files and save them to a DataFrame
df_data = pd.read_csv("calibration_data.csv")
df_labels = pd.read_csv("calibration_labels.csv")
#print(df_data.head())

#1-Hot-Encode the labels
df_labels['0'] = df_labels['0'].astype(str) #Turns int into str
df_labels = pd.get_dummies(df_labels) #1-hot-encode the categories
#print(df_labels.head())
print("OG shape:", df_data.shape)

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
X_train, X_test, y_train, y_test = train_test_split(df_data, df_labels, test_size=0.2, random_state=1377)
print('ya')

#Selecting paramaters
#param = {'criterion':['gini','entropy'], 'splitter':['best','random'], 'min_samples_split':[2,5,10,15], 'min_weight_fraction_leaf':[0,.5], 'min_impurity_decrease':[0,2,3,5]}

#Make the models
#clf = GridSearchCV(tree.DecisionTreeClassifier(random_state=420), param)
clf = tree.DecisionTreeClassifier(random_state=52)

#Train the model
start = time()
clf.fit(X_train, y_train)
print('yeet with a time of:', time() - start, 'seconds')

#Esting the model
y_pred = clf.predict(X_test)

#Evaluation
print("Accuracy Score:", accuracy_score(y_test, y_pred))

#Saveing the model
pkl_filename = "DecisionTree.pkl"  
with open(pkl_filename, 'wb') as file:  
    pickle.dump(clf, file)
print('Model saved')