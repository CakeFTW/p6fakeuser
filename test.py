import dataprocess as pro
import pandas as pd
data_set = pd.read_csv("dataframe_data.csv")
data_set_np = data_set.values

data_labels = pd.read_csv("dataframe_labels.csv")
print(data_set.describe())
data_labels['labels'] = data_labels['0'].astype(str)

label_one_hot = pd.get_dummies(data_labels['labels'])
data_labels_np = label_one_hot.values
print(data_set_np.shape)

pro.prep_nn(data_set_np, 720 , 320)
