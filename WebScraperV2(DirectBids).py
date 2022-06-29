




# we import the class that we need scraping our blog
from pydoc import text
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time


i=0
while i <= 0:                  #change 0 to number of loops you want +1
 i = i + 1                     #change 1 to 0 to loop forever
 # time.sleep(10)              #time delay in seconds
 

 response = requests.get("https://www.directbids.com/auctions")              #link to direct bids auction
 

 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("div", {"class": "grid-item"})

 filename = str(uuid.uuid4())
 print(filename)

 with open('Auction372;' + filename + '.csv', 'w' ) as csv_file:                #file name
     csv_writer = writer(csv_file)
     headers = ['Lot', 'Info', 'Photo', 'Bid', 'Title']
     csv_writer.writerow(headers)

     for post in posts:
        print('yup')

        
        Lot = post.find_all(class_='d-flex mb-1 small mb-2')
        print(Lot)

        Info = post.find('a')['href']      #
        print(Info)

        Photo = post.find(class_='grid-item-img')['src']        #
        print(Photo)

        Bid = post.find_all(class_='d-flex mb-1')
        print(Bid)

        Title = post.find(class_='grid-item-title')
        print(Title)

        csv_writer.writerow([Lot, Info, Photo, Bid, Title])
#There is no Asking Bid