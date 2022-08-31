from bs4 import BeautifulSoup
import requests
from csv import writer

class QuoteScrape:

    def request():
        html_text = requests.get('https://quotes.toscrape.com/').text #get html
        soup = BeautifulSoup(html_text, 'lxml') #parse html
        return soup

    def file_open():
        f = open("simple.csv", "w") #create file
        return f    

    def extract_ans(self):  
         
        g = QuoteScrape.file_open() #file open
        header = ('Quotes', 'Author', 'Tags')
        g.write(str(header) + '\n' + '\n') #print heading
        scrap = []
        x = QuoteScrape.request() #get parsed html
        qts = x.find_all('div', class_ = 'quote') 
        for d in qts:
            quotes = d.find('span', class_ = 'text').text
            author_name = d.find('small', class_ = 'author').text
            tags = d.find('div', class_ = 'tags').meta['content']
            scrap = [quotes, author_name, tags]

            g.write(str(scrap) + '\n' + '\n') #print scraps
        
        g.close()
    

qs = QuoteScrape() #class instance
qs.extract_ans() #call statement



