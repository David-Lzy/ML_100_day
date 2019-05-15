#https://raw.githubusercontent.com/MLEveryday/100-Days-Of-ML-Code/master/Info-graphs/Day%202.jpg

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Parent_directory(parent_number,file_location):#返回父级目录以及层数
    import os
    if parent_number == 0:
        return os.path.abspath(os.path.dirname(file_location))
    else:
        return Parent_directory(parent_number-1,os.path.dirname(file_location))

data_location = Parent_directory(1,__file__) + r'\datasets' + '\\' + r'studentscores.csv'
dataset = pd.read_csv(data_location) 

X = dataset.iloc[:,:1].values
X_1 = dataset.iloc.values
print(X)
print(X_1)