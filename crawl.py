import requests
from bs4 import BeautifulSoup, SoupStrainer

# returns a list of URLs found on a webpage
def getUrlFromOutlet(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")

	links = soup.find_all("a")
	outlet_links = []

	for link in links:
		outlet_links.append(link.get("href"))
	return outlet_links