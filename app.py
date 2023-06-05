from crawl import getUrlFromOutlet
from scrape import pullText
from clean import cleanText
from build_dataset import buildDataSet
#import plot_cloud

def main():
	outlet_to_url = {
	"FX_NEWS" : "https://www.foxnews.com/politics",
	"YAHOO" : "https://news.yahoo.com/politics/",
	"CBS": "https://www.cbsnews.com/politics/",
	"NBC" : "https://www.nbcnews.com/politics",
	"CNN" : "https://edition.cnn.com/politics",
	"CNBC" : "https://www.cnbc.com/politics/",
	"HUFF_POST": "https://www.huffpost.com/news/politics"
	}

	outlet_data = []

	for outlet in outlet_to_url:
		print(f"Crawling {outlet}")
		outlet_links = getUrlFromOutlet(outlet_to_url[outlet])
		outlet_text_list = []
		count = 0
		for link in outlet_links:
			count += 1
			outlet_text = pullText(link)
			cleaned_outlet_text = cleanText(outlet_text)
			generated_text_data = {"ouletId": outlet, "text": cleaned_outlet_text}
			outlet_data.append(generated_text_data)
			print("Appending to data set... "+ str(count))
			if count > 4:
				break
		print("building dataset...")
		buildDataSet(outlet_data, outlet)
		print("completed")
		break
	


		










if __name__ == "__main__":
	main()
	

