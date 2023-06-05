import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import sys

nltk.download('stopwords')

stopwords.words("english")


# split text into tokens (words)
def tokenizeText(text):
	return text.split(" ")

# remove non alphabetic text
def filterByAlphaList(lst):
	filtered_list = [word for word in lst if word.isalpha()]
	return filtered_list

# convert all text to lower 
def convertAllLower(lst):
	lower_list = [word.lower() for word in lst]
	return lower_list

# remove all stopwords
def removeStopWords(lst):
	filtered_words = [word for word in lst if word not in stopwords.words('english')]
	return filtered_words

# not used, but stemming or lemmatization can be used for certain use cases of this application
def stemWords(lst):
	ps = PorterStemmer()
	stemed_list = [ps.stem(word) for word in lst]
	return stemed_list

# wrapper function to export and clean  text
def cleanText(text):
	tokens = tokenizeText(text)
	lower_list = convertAllLower(tokens)
	no_stop_words = removeStopWords(lower_list)
	filtered_alpha_list = filterByAlphaList(no_stop_words)
	return filtered_alpha_list

   


