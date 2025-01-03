# -*- coding: utf-8 -*-
"""Feature Extraction from Text.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rwYYuTMilee-QXcPPNjr_W1YC6vdrxO9

"
Machine learning Algorithm can't take data in raw text.

We can use feature extraction from the raw text in order to pass
numerical features to the machine learning algorithm.

For example, we could count the occurence of each word to map
text to a number.

Count Vectorization

Term-Frequency and Inverse Document Frequency.


""

# Count Vectorization
"""

msg = ["Hey, lets go to the game today!",
       "Call your mom.",
       "Want to go walk your dogs?"]
msg

from sklearn.feature_extraction.text import CountVectorizer

vector=CountVectorizer()
vector

# Count the occurrences of all the unique words.

# It will treat each individual unique word as a feature.

# fit the vectorizer to our data

vector.fit(msg)
vector.get_feature_names_out()

#  Document Term Matrix(DTM)

# It's going to count the occurrence of each unique feature or word
# throughout every single document.

# And each document is essentially a just each text messages.

# So we can think of a term document as just another word
# for every documented text.

# Imagine a very large set of documents known as a corpus,
# we are going to have a very sparse matrix, a matrix with a lot of
# zeros. It is called document term matrix or DTM.

"""# TfidfVetorizer

An alternatice to CountVetorizer is something called TfidfVectorizer.
It also creates a document term matrix from our messages.

However, instead of filling with DTM with tokens counts it calculates
term frequency - inverse document frequency value for each word(TF-IDF)


Term frequency tf(t,d) :-
It is the raw count of a term in a document, i.e. the number of times
that term t occurs in document d.

However, Term Frequency alone is not enough for a thorough feature
analysis of the text!

Let's imagine very common terms , like "a" or "the"...

Because the term "the" is so common, term frequency will tend to
incorrectly emphasize which happen to use the word "the" more frequently.
without giving enough weight to the more meaningful terms "red" and "dogs"

An inverse document frequency factor is incorporated which diminishes
the weight of terms that occure very frequently in the document set and
increases the weight of terms that occur rarely.

It is the logarithmically scaled inverse fraction of the documents that
contain the word(obtained by dividing the total number of documents by
the number of documents containing the term, and then taking the
logarithm of that quotient.)

TF- IDF = term frequency * (1/document frequency)

TF- IDF = term frequency * inverse document frequency

"""
"""

from sklearn.feature_extraction.text import TfidfVectorizer
vector = TfidfVectorizer()
vector.fit(msg)

vector.get_feature_names_out()

dtm = vector.fit_transform(msg)
print(dtm.transpose())

# TF - IDF allows us to understand the context of words across an entire
# corpus of documents instead of just its relative importance in a
# single document.