# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:56:58 2018

@author: ADMIN
"""

import spacy
import pandas as pd
import string
from spacy.lemmatizer import Lemmatizer
punc = set(string.punctuation)

print('spaCy Version: %s' % (spacy.__version__))
nlp = spacy.load('en_core_web_sm',disable=['parser', 'ner'])
dataset = pd.read_csv('one_correct_three_wrong.tsv',delimiter='\t',encoding='utf-8')
x = dataset.iloc[:,1]
y = dataset.iloc[:,2]

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
#data3= x.apply(lambda x: ' '.join([word for word in x.split() if word not in (spacy_stopwords) ])).str.lower()
def normalize(comment, lowercase, remove_stopwords):
    if lowercase:
        comment = comment.lower()
    comment = nlp(comment)
    lemmatized = list()
    for word in comment:
        lemma = word.lemma_.strip()
        if lemma:
            #if not remove_stopwords or (remove_stopwords and lemma not in spacy_stopwords):
            lemmatized.append(lemma)
    return " ".join(lemmatized)

Data = x.apply(normalize, lowercase=True, remove_stopwords=False)


def remove_punc(x):
    for punctuation in string.punctuation:
        x = x.replace(punctuation, '')
    return x
df = data3.apply(remove_punc)
dataset = dataset.drop(x, 1, errors='ignore')
dataset = dataset.join(df)


spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
data31= y.apply(lambda x: ' '.join([word for word in x.split() if word not in (spacy_stopwords) ])).str.lower()
def remove_punc(z):
    for punctuation in string.punctuation:
        z = z.replace(punctuation, '')
    return z
df1 = data31.apply(remove_punc)
z = dataset.iloc[:,1]
dataset = dataset.drop(['The AR gene provides instructions for making a protein called an androgen receptor. Androgens are hormones (such as testosterone) that are important for normal male sexual development before birth and during puberty.Androgen receptors allow the body to respond appropriately to these hormones.ome mutations lead to an abnormally short version of the androgen receptor protein, while others result in the production of an abnormal receptor that cannot bind to androgens or to DNA. As a result, cells that are sensitive to androgens become less responsive to these hormones or unable to use these hormones at all.'], 1, errors='ignore')
dataset = dataset.join(df1)


