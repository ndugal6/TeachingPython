from urllib import request #a different way to import, explained later

#fetch a csv file link from online, I got googles stock price history csv(comma separated value file)
goog_url = "http://chart.finance.yahoo.com/table.csv?s=GOOG&a=9&b=14&c=2016&d=10&e=14&f=2016&g=d&ignore=.csv"


def download_stock_data(csv_url):
#Connect
    response = request.urlopen(csv_url)     #going to url and storing connection to webpage in variable response
    csv = response.read()                   #reading and storing all the data
#Save as a String
    csv_str = str(csv)
    lines = csv_str.split("\\n")            #split breaks up super long string at breaks
#Make file on Computer
    dest_url = r'goog.csv'                  #remember to put r before file paths, ensures raw string
    fx = open(dest_url, "w")                #Opens and creates file to write to
#Write to file on Computer
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)
