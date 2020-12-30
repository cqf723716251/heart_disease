#import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

#import the read the dataset
heart= pd.read_csv('heart.csv')
head = heart.head()
# heart_describe = heart.describe()
heart_info = heart.info()
heart_unique = heart.nunique()
target_count = heart['target'].value_counts()

#convert columns to category since values are discrete
columns_to_category= ['sex', 'cp', 'fbs', 'restecg','exang', 'slope', 'ca', 'thal', 'target']
heart[columns_to_category]= heart[columns_to_category].astype('category') # Dtype changed to category
heart_describe = heart.describe() # category columns are excluded
