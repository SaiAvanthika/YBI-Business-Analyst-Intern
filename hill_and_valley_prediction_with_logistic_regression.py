# -*- coding: utf-8 -*-
"""Hill and Valley Prediction with Logistic Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ljbsUNOsvsQ-2DTAtjgjr09gh1Ul7PE_

# **Hill and Valley Prediction with Logistic Regression**

# Import Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# Import data"""

df = pd.read_csv("https://raw.githubusercontent.com/YBIFoundation/Dataset/main/Hill%20Valley%20Dataset.csv")

df.head()

df.describe()

df.info()

df.columns

df.shape

"""# define target (y) and features (x)"""

df.columns

df['Class'].value_counts()

df.groupby('Class').mean()

y=df['Class']

y.shape

y

x=df[['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10','V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20','V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30','V31', 'V32', 'V33', 'V34', 'V35', 'V36', 'V37', 'V38', 'V39', 'V40','V41', 'V42', 'V43', 'V44', 'V45', 'V46', 'V47', 'V48', 'V49', 'V50','V51', 'V52', 'V53', 'V54', 'V55', 'V56', 'V57', 'V58', 'V59', 'V60','V61', 'V62', 'V63', 'V64', 'V65', 'V66', 'V67', 'V68', 'V69', 'V70','V71', 'V72', 'V73', 'V74', 'V75', 'V76', 'V77', 'V78', 'V79', 'V80','V81', 'V82', 'V83', 'V84', 'V85', 'V86', 'V87', 'V88', 'V89', 'V90','V91', 'V92', 'V93', 'V94', 'V95', 'V96', 'V97', 'V98', 'V99', 'V100']]

x=df.drop(['Class'],axis=1)

x.shape

x

"""plot of first 2 rows"""

plt.plot(x.iloc[0,:])
plt.title("Valley")

plt.plot(x.iloc[1,:])
plt.title("Hill")



"""# Standardizing X variables"""

from sklearn.preprocessing  import StandardScaler

ss=StandardScaler()

x=ss.fit_transform(x)

x

x.shape

"""# Train Test Split"""

from sklearn .model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6,random_state=1507)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

"""# Select model"""

from sk.learnlinearmodel import LogisticRegression