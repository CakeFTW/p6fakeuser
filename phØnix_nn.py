from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from time import time
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


print("tensor-boi running")
data_set = pd.read_csv("dataframe_data.csv")

data_labels = pd.read_csv("dataframe_labels.csv")
data_labels
print(data_set.describe())
data_labels['labels'] = data_labels['0'].astype(str)

label_one_hot = pd.get_dummies(data_labels['labels'])

# plt.scatter( range(100), range(100), c='r')
# plt.show()
print(data_set.head())

x_train,x_test,y_train,y_test = train_test_split(data_set,label_one_hot, test_size = 0.33, random_state = 42)


#create model
classifier = Sequential()
#First Hidden Layer
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal', input_dim=75))
#Second  Hidden Layer
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dropout(0.5))
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(12, activation='relu', kernel_initializer='random_normal'))


#third  Hidden Layer

#Output Layer
classifier.add(Dense(6, activation='sigmoid', kernel_initializer='random_normal'))

classifier.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

classifier.fit(x_train,y_train, epochs=200, batch_size= 10)

starttime = time()
scores = classifier.evaluate(x_test, y_test)
print("traintime : ", (time() - starttime)/len(y_test) , "per example")
print("\n%s: %.2f%%" % (classifier.metrics_names[1], scores[1]*100))
print(len(y_test))

