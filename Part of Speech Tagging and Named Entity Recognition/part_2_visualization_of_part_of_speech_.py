# -*- coding: utf-8 -*-
"""Part -2  Visualization of Part of Speech .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QmTWl2ZCR_y3etbqyxHvmhQ3eEBvZ2bW

# Visualization of Part of Speech
"""

# Visualize Parts of Speech strcture with displacy

import spacy
nlp=spacy.load("en_core_web_sm")

doc = nlp(u'The quick brown fox jumped over the lazy dog')

from spacy import displacy

displacy.render(doc,style='dep')

options = {'distance':100,'compact':'True','color':'red','bg':'black',\
           'font':'Times'}


displacy.render(doc,style='dep',options=options)

# If we are dealing with large texts,
# displacy.serve is meant to accept a single document or a list of
# documents.
# Since large texts are difficult to view online we can pass a list of
# spans instead

doc2 =nlp(u'USA has the most powerful military and economy.\
After that Russia is second largest military superpower.\
The comes China and India with growing military and economic capabilities')

spans = list(doc2.sents)
spans

displacy.serve(spans,style='dep',options=options)