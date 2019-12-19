"""Module with function for tranforming data"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import statsmodels.api as sm
from imblearn.over_sampling import SMOTE
from collections import Counter
from yellowbrick.classifier import ROCAUC
from yellowbrick.classifier import ConfusionMatrix
from yellowbrick.classifier import ClassificationReport
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
np.random.seed(42)

nh_cols = ['SUBDIV',
 'NORC',
 'NEARBARCL',
 'NEARABAND',
 'NEARTRASH',
 'RATINGNH',
 'NHQSCHOOL',
 'NHQPCRIME',
 'NHQSCRIME',
 'NHQPUBTRN',
 'NHQRISK', 
 'ADEQUACY']

def create_dataset():
    """Transforms household.csv file from AHS to neighbor-related columns plus target variable (ADEQUACY_BIN)"""
    df = pd.read_csv('data/household.csv')
    df = df[nh_cols]
    for column in df.columns:
        df[column] = df[column].astype(str).str.replace("'","")     # removing quotation marks from df
    df = df.apply(pd.to_numeric, errors='ignore')
    df['ADEQUACY_BIN'] = df.ADEQUACY.map(lambda x: 0 if x>1 else 1)
    df.drop('ADEQUACY', axis=1, inplace=True)
    return df

def export_dataset(df):
    """Exports data as 'ahs.csv' to data folder"""
    print("Exporting data as 'ahs.csv' to data folder")
    df.to_csv('data/ahs.csv', index=False)
    print('Done!')
    
        

    