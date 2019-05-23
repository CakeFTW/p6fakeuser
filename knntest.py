import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from time import time
import pickle
import dataprocess

#data_set = pd.read_csv("dataframe_data.csv")

#Read the data and labels csv files and save them to a DataFrame
df_data = pd.read_csv("ep_noflip_data.csv")
df_labels = pd.read_csv("ep_noflip_labels.csv")
#print(df_data.head())

#1-Hot-Encode the labels
df_labels['0'] = df_labels['0'].astype(str) #Turns int into str
df_labels = pd.get_dummies(df_labels) #1-hot-encode the categories

pd_data =df_data.values
pd_data = dataprocess.circle_scale(pd_data)

x_train,x_test,y_train,y_test = train_test_split(pd_data,df_labels, test_size = 0.33, random_state = 42)


# myList = list(range(1,50))
# neighbors=list(filter(lambda x: x%2 !=0, myList))
# cv_scores=[]
# for k in neighbors:
#     knn=KNeighborsClassifier(n_neighbors=k)
#     scores=cross_val_score(knn, x_train, y_train,scoring='accuracy',cv=15)
#     cv_scores.append(scores.mean())
#     print(scores.mean())
# MSE=[1-x for x in cv_scores]
# optimal_k=neighbors[MSE.index(min(MSE))]
# print(optimal_k){}

knn=KNeighborsClassifier(n_neighbors=1)


#loaded = pickle.load(open('knn.sav', 'rb'))
knn.fit(x_train, y_train)
# a=time()
pred=knn.predict(x_test)
print(accuracy_score(y_test,pred))
print(pred[0])
pickle.dump(knn, open('knn_final.sav', 'wb'))