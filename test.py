import re
import sys
import csv

from collections import Counter


from nltk.corpus import stopwords
from nltk.stem import porter

STOPWORDS = set(stopwords.words('english'))
STEMMER = porter.PorterStemmer()
LIMIT = 500


def clean(tweet):

    tweet = (re.sub(r"#[\w\d]*|@[.]?[\w\d]*[\'\w*]*|https?:\/\/\S+\b|\
             www\.(\w+\.)+\S*|[.,:;!?()$-/^]*", "", tweet).lower())

    # get rid of all tags

    tweet = re.sub(r"(.)\1\1{1,1}", "", tweet)
    tweet = (re.sub(r"($.)\1{1,}", "", tweet).split())

    tweet = [STEMMER.stem_word(x) for x in tweet if
             x not in STOPWORDS and len(x) > 1]


    return tweet
