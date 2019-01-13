# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 00:42:03 2018

@author: ADMIN
"""

import nltk
nltk.download('wordnet')
import pandas as pd
import string
#from nltk.stem.snowball import SnowballStemmer
punc = set(string.punctuation)

dataset = pd.read_csv('eval2_unlabelled.tsv',delimiter='\t',encoding='utf-8')


w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()
def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in nltk.word_tokenize(text)]

#data3= x.apply(lambda x: ' '.join([word for word in x.split() if word not in (lemmatize_text) ])).str.lower()
df= dataset['question'].apply(lambda x:' '.join(lemmatize_text(x))).str.lower()
#stemmer = SnowballStemmer("english")
'''def lemmatize_text_again(text):
    return [lemmatizer.lemmatize(w) for w in stemmer.stem(text)]
df1= df.apply(lambda x:' '.join(lemmatize_text_again(x)))

def remove_punc(x,pattern):
    for punctuation in pattern:
        x = x.replace(punctuation, ' ')
    return x
def remove_punct(x,pattern):
    
    for punctuation in pattern:
        x = x.replace(punctuation, x)
        return x      
'''
'''import re
def remove_before_token(sentence, keep_apostrophe = False):
    sentence = sentence.strip()
    if keep_apostrophe:
        PATTERN = r'[#|$|&|%|@|~]'
        filtered_sentence = re.sub(PATTERN, r' ', sentence)
    else :
        PATTERN = r'[^a-zA-Z0-9]'
        filtered_sentence = re.sub(PATTERN, r' ', sentence)
    return(filtered_sentence)

ccc'''
pattern = ['[^!:,;)(.?]+']
import re
def remove_punct(x,pattern):
    
    for punctuation in pattern:
        x = re.findall(punctuation, x)
        return x 
    return ('\n')
data= df.apply(lambda x:''.join(remove_punct(x,pattern)))
dataset = dataset.drop('question' , axis = 1,errors='ignore')
dataset = dataset.join(data)


df2= dataset['result'].apply(lambda x:' '.join(lemmatize_text(x))).str.lower()
#df3= df2.apply(lambda x:' '.join(lemmatize_text_again(x)))
data1= df2.apply(lambda x:''.join(remove_punct(x,pattern)))

#data1= df2.apply(remove_punct)
dataset = dataset.drop('result' , axis = 1,errors='ignore')
dataset = dataset.join(data1)

#dataset = dataset.drop('unknown' , axis = 1,errors='ignore')
dataFinal = dataset.to_csv('modified_eval2_unlabelled_v2.tsv',index = False,sep = '\t', header=False)
