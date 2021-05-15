import numpy as np # linear algebra
import pandas as pd #data processing

import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def get_all_query(title, author, text):
    total= title + author + text
    total = [total]
    return total

def remove_punctuation_stopwords_lemma(sentence):
	stop_words = stopwords.words('english')
	lemmatizer = WordNetLemmatizer()
	filter_sentence = ''
	sentence = re.sub(r'[^\w\s]','',str(sentence))
	words = nltk.word_tokenize(sentence)
	words = [w for w in words if not w in stop_words]
	for word in words:
		filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
	return filter_sentence
