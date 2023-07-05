import os
import math
import torch
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint
from sklearn.base import BaseEstimator
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score

# Prepare data

students_mat = pd.read_csv(os.path.join('data', 'student-mat.csv'))
students_por = pd.read_csv(os.path.join('data', 'student-por.csv'))

students = pd.concat([students_mat, students_por], axis=0)
students['grade'] = (students['G1'] + students['G1'] + students['G3']) / 3
students['alc'] = students['Walc'] + students['Dalc']
students = students.drop(columns=['G1', 'G2', 'G3', 'school'])
students.head(5)

# categorical

categorical_dict = {}
for col in students.columns:
    if students[col].dtype == 'object':
        le = LabelEncoder()
        students[col] = le.fit_transform(students[col])
        categorical_dict[col] = dict(
            zip(le.classes_, le.transform(le.classes_)))

pprint(categorical_dict)
