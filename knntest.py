import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from time import time
import pickle

data_set = pd.read_csv("dataframe_data.csv")

data_labels = pd.read_csv("dataframe_labels.csv")
data_labels
print(data_set.describe())
data_labels['labels'] = data_labels['0'].astype(str)
print(data_set.head())
label_one_hot = pd.get_dummies(data_labels['labels'])

x_train,x_test,y_train,y_test = train_test_split(data_set,label_one_hot, test_size = 0.33, random_state = 42)


# myList = list(range(1,50))
# neighbors=list(filter(lambda x: x%2 !=0, myList))
# cv_scores=[]
# for k in neighbors:
#     knn=KNeighborsClassifier(n_neighbors=k)
#     scores=cross_val_score(knn, x_train, y_train,scoring='accuracy',cv=10)
#     cv_scores.append(scores.mean())
#     print(scores.mean())
# MSE=[1-x for x in cv_scores]
# optimal_k=neighbors[MSE.index(min(MSE))]
# print(optimal_k)
# plt.plot(neighbors,MSE)
# plt.show()

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
a=time()
pred=knn.predict(x_test)
print(accuracy_score(y_test,pred))
print((time()-a)/len(x_train))

pickle.dump(knn, open('knn.sav', 'wb'))
loaded = pickle.load(open('knn.sav', 'rb'))
