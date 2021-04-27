import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
np.random.seed(77)
def make_lower(text):
    "Converts all text to lower case"
    return text.lower()

def tokenize(text):
    "Tokenizes text"
    return word_tokenize(text)

def lemmatizer(text):
    tag_map = defaultdict(lambda : wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV  
    word_Lemmatized = WordNetLemmatizer()
    final_words = []
    for word, tag in pos_tag(text):
        if word not in stopwords.words('english') and word.isalpha():
            word_final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
            final_words.appen(word_final)
    return final_words

def clean_text(dataframe):
    "Module to clean text for baseline model"
    dataframe['tweets'].dropna(inplace = True)
    dataframe['tweets'] = dataframe['tweets'].apply(make_lower)
    dataframe['tweets'] = dataframe['tweets'].apply(tokenize)
    dataframe['tweets'] = dataframe['tweets'].apply(str)
    return dataframe



