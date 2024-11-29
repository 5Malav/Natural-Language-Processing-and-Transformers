# -*- coding: utf-8 -*-
"""Project - 3 Movie Reviews.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z5QcP855oulc_u8WxR_HSERSWyrDZMB_
"""

import pandas as pd
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# load the data

data= pd.read_csv("/content/moviereviews.tsv",sep="\t")
data.head()

data.info()

data.isnull().sum()

data['label'].value_counts()

# drop null values

data.dropna(inplace=True)

blanks=[]

for i ,lb,rv in data.itertuples():

    if type(rv)==str:
        if rv.isspace():
            blanks.append(i)

len(blanks)

# drop spaces

data.drop(blanks,inplace=True)

data['label'].value_counts()

sid= SentimentIntensityAnalyzer()
sid

data['scores']= data['review'].apply(lambda review:sid.polarity_scores(review))
data.head()

data['compound']=data['scores'].apply(lambda d:d['compound'])
data.head()

data['scores'][1]

data['comp_score']=data['compound'].apply(lambda score:"pos" if score>=0 else "neg")
data.head()

from sklearn.metrics import confusion_matrix,classification_report

confusion_matrix(data['label'],data['comp_score'])

report= classification_report(data['label'],data['comp_score'],output_dict=True)
report

report=pd.DataFrame(report).transpose()
report

# not a good score for neg review.

# accuracy is also only 64%.