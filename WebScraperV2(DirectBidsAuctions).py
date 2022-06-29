
# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time

i=0

filename = str(uuid.uuid4())
print(filename)

with open('DirectBidsAuction;' + filename + '.csv', 'w' ) as csv_file:         #file name
 headers = ['Lot', 'Info', 'Photo', 'Bid', 'Title']


 while i <= 1:                  #change 0 to number of loops you want +1 and pages to go through
     i = i + 1   
     print(i)
     time.sleep(0)              #time delay in seconds

     response = requests.get("https://www.directbids.com/auctions")              #link to direct bids auction
     soup = BeautifulSoup(response.text, 'html.parser')
     posts = soup.find_all("li", {"class": "grid-item"})

     print('Stage 1')

     for post in posts:
        print('Stage 2')
        
        csv_writer = writer(csv_file)
        
        Lot = soup.findAll('div' ,attrs={"class" : "d-flex mb-1 small mb-2"})
        print(Lot)

        Info = post.find('a')['href']      #
        print(Info)

        Photo = post.find(class_='grid-item-img')['src']        #
        print(Photo)

        Bid = post.find(class_='d-flex mb-1')
        print(Bid)

        Title = post.find(class_='grid-item-title')
        print(Title)


        csv_writer.writerow([Lot, Info, Photo, Bid, Title])
 csv_writer.writerow(headers)
print('Stage 3')
