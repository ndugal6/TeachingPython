import random #when dowloading image, giving it random name
import urllib.request #allows us to get data from a website

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg" #Cast the number to a String
    urllib.request.urlretrieve(url, full_name)

#Downloads and saves the image as a jpg into the working directory
download_web_image("https://scontent-dft4-1.xx.fbcdn.net/v/t1.0-9/13680571_10207767142509537_4408524643039459221_n.jpg?oh=a5bc08f55654546a68ce2e4dcfacb73c&oe=58900B18")