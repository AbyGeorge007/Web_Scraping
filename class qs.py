from bs4 import BeautifulSoup
import requests
from csv import writer

class QuoteScrape:

    def request():
        html_text = requests.get('https://quotes.toscrape.com/').text
        return html_text

    def file_open():
        f = open("try1.csv", "w")
        return f    

    def extract_ans(self):  
         
        g = QuoteScrape.file_open()
        header = ('Quotes', 'Author', 'Tags')
        g.write(str(header) + '\n' + '\n')

        scrap = []
        x = QuoteScrape.request()
        soup = BeautifulSoup(x, 'lxml')
        qts=soup.find_all('div', class_ = 'quote')
        for d in qts:
            quotes = d.find('span', class_ = 'text').text
            author_name = d.find('small', class_ = 'author').text
            tags = d.find('div', class_ = 'tags').meta['content']
            scrap = [quotes, author_name, tags]

            g.write(str(scrap) + '\n' + '\n')
        
        g.close()
    

qs = QuoteScrape()
qs.extract_ans()




