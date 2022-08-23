from bs4 import BeautifulSoup
import requests
from csv import writer


with open('scraps.csv', 'w') as f:
    thewriter = writer(f)
    header = ['Quotes', 'Author', 'Tags'] 
    thewriter.writerow(header)
    scrap = []
    html_text = requests.get('https://quotes.toscrape.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find('div', class_ = 'col-md-8')
    for div in divs:
        qts=soup.find_all('div', class_ = 'quote')
        for d in qts:
            quotes = d.find('span', class_ = 'text').text
            author_name = d.find('small', class_ = 'author').text
            tags = d.find('div', class_ = 'tags').meta['content']
            scrap = [quotes, author_name, tags]
            thewriter.writerow(scrap)
