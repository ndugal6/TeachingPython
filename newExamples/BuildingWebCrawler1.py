import requests
from bs4 import BeautifulSoup

#Create the spider
def trade_spider(max_pages):
    page = 0
    while page <= max_pages:
        #request data from website
        #Convert into plain text (get source code)
        #Turn into BeautifulSoup
        url = 'https://www.reddit.com/?count=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html5lib")
        #Soup is set up so we can search through it
        for link in soup.findAll('a', {'data-event-action':'title'}):
            #finds html tag a with matching key:values insdie
            href = 'https://www.reddit.com/?count=' + link.get('href')
            title = link.string
            print(title)
            # print(href)
            get_single_item_data(href)
        page += 20

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for item_name in soup.findAll('time', {'class':'live-timestamp'}):
        print(item_name.string)
    for links in soup.findAll('a'):
        try :
            href = 'https://www.reddit.com/?count=' + links.get('href')
        except TypeError:
            print("Post's link error")

        print(href)





trade_spider(40)