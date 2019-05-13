import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def Parent_directory(parent_number,file_location):#返回父级目录以及层数
    import os
    if parent_number == 0:
        return os.path.abspath(os.path.dirname(file_location))
    else:
        return Parent_directory(parent_number-1,os.path.dirname(file_location))

#print(Parent_directory(1,__file__))

data_location = Parent_directory(1,__file__) + r'\datasets' + r'\Data.csv'


dataset = pd.read_csv(data_location)#读取csv文件
#print(dataset)
X = dataset.iloc[:,:-1].values#-1从右向左
Y = dataset.iloc[ : ,-1].values

imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])


print(X)
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
#对本身不可量化的特征进行数字化
#print(X)

'''onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
print(X)'''
#print(X)
X = OneHotEncoder(categories='auto').fit_transform(X).toarray()
#print(X)

#print(Y)
Y =  LabelEncoder().fit_transform(Y)
#print(Y)

X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)#random_state随机数种子
#print(X_train, X_test, Y_train, Y_test)


sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
#print(X_train)