# -*- coding: utf-8 -*-
"""Topic Modeling  .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pBHY2FhPcN3dvFHjxXLuCjgpOlyIo_-i

# Topic Modeling

Topic Modeling allows for us to efficiently analyze large volumes of
text by clustering documents into topics.

A large amount of text data in unlabeled meaning we will not be able
to apply Supervised machine learning models would actually depend
on historical label data.

And in the real world, specifically for text data, we are not gonna
have a convenient label attached to a text data set, such as
positve or negative, or spam vs. ham.

Instead , we may have variety of labels such as different categories
that a newspaper article could be in and we may just have the test
itself unlabeled.

So its up to us to try to discover those labels through Topic Modeling.

If we have unlabeled data, then we can attempt to "discover" labels.

In the case of text data, this means attempting to discover clusters
of attempting to discover clusters of documents, grouped together by \
topic.

A very important to keep in mind here is that we don't know the "correct"
topic or "right anwer"!

All we know is that the document clustered together share similar topic
ideas.

It is up to us to identify what these topics really represent.

"

# Latent Dirichlet Allocation

Johann Peter Gustav Lejeune Dirichlet was a German mathmatician in the
1980s who contributed widely to the field of modern mathematics.

There is a probability distribution named after him "Dirichilet Distribution"

Latent Dirichlet Allocation is based off this probability distribution.

In 2003 LDA was first published as a graphical model for topic discovery
a Journal of Machine Learning Research by David Blei, Andrew Ng and
Michael I. Jordan.

Assumptions of LDA for TOpic Modeling:-

1.) Documents with similar topics use similar groups of words.

2.) Latent topics can then be found by searching for groups of words that
frequently occure together in documents across the corpus.

Think of these 2 assumptions mathematically.

Documents are probabiluity distributions over latent topics.

Topics themselves are probability distributions over words.

We can imagine that any particular document is going to have a
probability distribution over a given amount of latent topics.

So let's say, we decide that there are five latent topics across
various documents.

Then any particular document is going to have a probability of
belonging to each topic.

Topics themselves are probability distributions over words.

LDA represents documents as mixtures of topics that spit out words
with certain probabilities

It assumes that documents are produced in the following fashion:1.

1.) Decide on the number of words N the document will have.

2.) Choose a topic mixture for the document(according to a Dirichilet
distribution over a fixed set of K topics.)
For example:- 60% business, 20%v politics and 10% food.

Generate each word in the document by:

1.) FIrst picking a topic according to the multinomial distribution that
we sampled previosuly (60% business, 20% politics, 10% food)

2.) Using the topic to genrate the word itself(according to the topic's
multinomial distribution)

For example, if we selected food topic, we might generate the word
"apple" with 60% probability , "home" with 30% probability and so on.

Assuming this generative model for a collection of documents , LDA then
tries to backtrack from the document to find a set of topics that are
likely to have generated collection.

Now imagine we have a set of documents.

we have chosen some fixed number of K topics to discover, and want to
use LDA to learn the topic representation of each document and the words
associated to each topic.

Go through each document, and randomly assign each word in the
document to one of the K topics.

This random assignment already gives you both topic representations
of all the document and word distribution of all the topics.
(Note:- This initial topics won't make sense)
They are gonnna be really poor representation of topics since we
just essentially assigned every word a random topic.

Now we iterate over every word in every document to improve these topics.

For every word in every document and for each topic t we calculate:

p(topic t | document d) = the proportion of word in document d that
are currently assigned to topic t.

p(word w | topic t) =  the proportion of assignements to topic t over
all documents that come from this word w.

Reassign w a new topic, where we choose topic t with probability
p(topic t | document d) * p(word w | topic t)

This nis the probability that topic t generated word w.

After repeating the previous step a large number of times, we
eventually reach a roughly state where the assignment are acceptable.

At the end we have each document assigned to a topic.

We also can search for the words that have the highest probility of being
assigned to a topic.

We end up with an output such as:

Document assigned to Topic #4.

Most common words(highest probability) for Topic #4.
["cat", "vet", "birds", "dog" ...,"food","home"]

It is upto us to interprete these topics.

Two important notes:

The use must decide on the amount of topics present in the document.

The use must interpret what the topics are.

""
"""