from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
import streamlit as st
import pickle 

import pandas as pd
import numpy as np


df = pd.read_csv('water_potability3.csv')

X = df.iloc[:, :-1].values
y = df.iloc[:, 9].values


X_train7, X_test7, y_train7, y_test7 = train_test_split(X, y)

svc_classifier = SVC()
svc_classifier.fit(X_train7, y_train7)

pickle.dump(svc_classifier,open('svc_classifier.pkl','wb'))