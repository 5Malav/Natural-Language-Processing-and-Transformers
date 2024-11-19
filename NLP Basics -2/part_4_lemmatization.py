# -*- coding: utf-8 -*-
"""Part - 4 Lemmatization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X-vwPAI1wPoqzs-NYkYiBehM8S7n1mVa

# Lemmatization

In contrast to stemming, lemmatization looks beyond word reduction, and
considers a language's full vocabulary to apply a morphological analysis
to words.

The lemma of "was" is "be" and the lemma of "mice" is "mouse".
Further, the lemma of "meeting" might be "meet" or "meeting"
depending on its use in a sentence.

Here we are not just shortening words or cutting off the end of them.
Instead, we are looking at the full context of the word.

Lemmatization is typically seen as much more informative than simple
stemming which is why Spacy has opted to only have Lemmatizaation available
instead of Stemming.

Lemmatization looks at surrounding text to determine a given word's
part of speech, it does not categorize pharases.


""
"""

import spacy

nlp = spacy.load('en_core_web_sm')

doc1 = nlp(u'To get more healthy body I do running and walking. After running \
I do some yoga as well.')

for token in doc1:
    print(token.text," \t",token.pos_,'\t',token.lemma,'\t',token.lemma_)

def lemma(text):

    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}}\
        {token.lemma_}')

lemma(doc1)

doc2 =nlp(u'Artificial Intelligence (AI) enables machines to mimic human cognitive functions like learning, reasoning, and problem-solving. It powers applications such as voice assistants, autonomous vehicles, and data analytics. AI is transforming industries by automating tasks and providing intelligent insights.')

lemma(doc2)