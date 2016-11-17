import requests
from bs4 import BeautifulSoup
import operator

#This program finds the frequency of words on webpages

#Get list of all words on webpage

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html5lib')
    for post_text in soup.findAll('a', {'data-event-action' : 'title'}):
        #Gets just the string inside of it, removing all html and links
        content = post_text.string
        #Content is long string of everything, lower() lowercases everything, then split seperates at each space
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
        clean_up_list(word_list)


def clean_up_list(word_list):
    #Removes all symbols and junk from word list
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+-=[];'/{}:\"<>"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

#Create dictionary with all words and their frequency

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        #itemgetter(0) sorts by word, itemgetter(1) sorts by frequency
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

start('https://www.reddit.com/')
