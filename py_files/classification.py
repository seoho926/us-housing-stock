"""Module with classification functions"""

# Import libraries and set defaults
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import statsmodels.api as sm

from imblearn.over_sampling import SMOTE
from collections import Counter

from yellowbrick.classifier import ROCAUC
from yellowbrick.classifier import ConfusionMatrix
from yellowbrick.classifier import ClassificationReport
from yellowbrick.style.palettes import PALETTES, SEQUENCES, color_palette
color_palette(palette='flatui', n_colors=8)
from yellowbrick.style import set_palette
set_palette('pastel')

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sns.set_context('talk')
sns.set_style('ticks')
sns.set_palette('RdBu')
np.random.seed(42)

import warnings 
warnings.filterwarnings('ignore')


def SMOTE_graph(target,title,x=6,y=2):
    """Creates graph showing distribution of variable"""
    plt.figure(figsize=(x,y))
    ax = target.value_counts().plot(kind='barh',color='gray')
    ax.set_yticklabels(['Adequate','Inadequate'])
    ax.set_xlabel('Count')
    plt.title(title)
    return plt.show();

update_labels = {'RATINGNH': 'Neighborhood Rating',
 'NHQPCRIME': 'Petty Crime',
 'NEARTRASH': 'Presence of Trash',
 'NEARABAND': 'Presence of Abandoned Blgs',
 'SUBDIV': 'In Subdivision',
 'NEARBARCL': 'Presence of Bars on Windows',
 'NHQSCRIME': 'Serious Crime',
 'NORC': 'Majority Neighbors 55+',
 'NHQSCHOOL': 'Quality of Schools',
 'NHQPUBTRN': 'Quality of Public Transit',
 'NHQRISK': 'Risk of Natural Disasters'}

def features_graph_nb(feats,model_type):
    """Creates graph showing importance of features for each model"""
    viz = pd.DataFrame.from_dict(feats, orient='index').rename(columns={0: 'Importance'})
    viz['Importance'] = viz['Importance'].map(lambda x: abs(round(x, 2)))
    viz.sort_values(by='Importance', inplace=True, ascending=False)
    viz.reset_index(inplace=True)
    viz['Features'] = viz['index'].map(update_labels)
    viz.columns = ['AHS_ft', 'Importance', 'Features']
    ax = sns.barplot(y='Features', x='Importance', data=viz,color='gray');
    plt.title(f'Feature Importance for Housing Adequacy ({model_type})',size=20);
    plt.yticks(size=14);
    plt.xticks(size=14);
    return plt.show();