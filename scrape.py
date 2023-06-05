from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import urllib.request

# helper function to identify visible text on a page
def tagVisible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# pulls all text from a webpage
def textFromHtml(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tagVisible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


def pullText(url):
	html = urllib.request.urlopen('https://www.washingtonpost.com/business/2023/05/30/debt-ceiling-republicans-house-mccarthy/').read()
	return textFromHtml(html)





