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
import pandas as pd
import dataprocess as dp


print("tensor-boi running")
data_set = pd.read_csv("calibration_data.csv")
data_set_np = data_set.values
data_set_np = dp.circle_scale(data_set_np)

data_labels = pd.read_csv("calibration_labels.csv")
print(data_set.describe())
data_labels['labels'] = data_labels['0'].astype(str)

label_one_hot = pd.get_dummies(data_labels['labels'])
data_labels_np = label_one_hot.values
print(data_labels_np)
print(data_set_np.shape)

# plt.scatter( range(100), range(100), c='r')
# plt.show()

x_train,x_test,y_train,y_test = train_test_split(data_set_np,data_labels_np, test_size = 0.33, random_state = 42)

print(x_train[1])
print(x_train[1].shape)

drop_out = 0.1
#create model
classifier = Sequential()
#First Hidden Layer
classifier.add(Dense(128, activation='relu', kernel_initializer='random_normal', input_dim=75))
classifier.add(Dropout(drop_out))
#Second Hidden Layer
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dropout(drop_out))
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dropout(drop_out))
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dropout(drop_out))
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dropout(drop_out))
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dropout(drop_out))
classifier.add(Dense(64, activation='relu', kernel_initializer='random_normal'))


#third  Hidden Layer

#Output Layer
classifier.add(Dense(6, activation='softmax', kernel_initializer='random_normal'))

classifier.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

classifier.fit(x_train,y_train, epochs=200, batch_size= 128, validation_data = (x_test,y_test))

starttime = time()
scores = classifier.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (classifier.metrics_names[1], scores[1]*100))
scores = classifier.evaluate(x_test, y_test)
print("\n%s: %.2f%%" % (classifier.metrics_names[1], scores[1]*100))

file = open(r"C:\Users\Rasmus\Downloads\openpose-1.4.0-win64-gpu-binaries_recommended\openpose-1.4.0-win64-gpu-binaries\model_test1557825038\000000000177_keypoints.json", 'r')
import json
data = json.load(file)['people'][0]['pose_keypoints_2d']
print(data[1])
arrayz = np.zeros((1,75))


arrayz[0] = data
print(arrayz[0])


print(classifier.predict_classes(arrayz))
classifier.save('nn.h5')