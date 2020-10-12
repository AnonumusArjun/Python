from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
from sys import argv

class Analysis:
	def __init__(self, term):
		self.term = term
		self.subjectivity = 0
		self.sentiment = 0
		self.url ='https://www.google.com/search?q={0}&source=lmns&tbm=nws'.format(self.term)

	def run(self):
		response = requests.get(self.url)
		print(response.text)
		#soup = BeautifulSoup(response.text, 'html.parser')
		headline_result = soup.find_all('div', class_='st')
		for h in headline_result:
			blob = TextBlob(h.get_text())
			self.sentiment += blob.sentiment.polarity / len(headline_result)
			self.subjectivity += blob.sentiment.subjectivity / len(headline_result)


a = Analysis(argv[1])
a.run()
print(a.term, 'Subjectivity :', a.subjectivity, 'Sentiment: ', a.sentiment)