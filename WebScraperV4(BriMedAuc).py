
# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time

time.sleep(0)

i=0

filename = str(uuid.uuid4())
print(filename)

with open('BritishMedicalAuctions;' + filename + '.csv', 'w' ) as csv_file:         #file name
 headers = ['Lot', 'Bid', 'Title', 'Info', 'Photo']
 csv_writer = writer(csv_file)   
 csv_writer.writerow(headers)

 while i <= 0:                  #change 0 to number of loops you want +1 and pages to go through
     i = i + 1   
     print(i)
     time.sleep(600)              #time delay in seconds

     response = requests.get("https://auctions.britishmedicalauctions.co.uk/auctions/catalog/id/521/June-2022-Endoscopy-Part-2" + str(i))              #link to direct bids auction
     soup = BeautifulSoup(response.text, 'html.parser')
     posts = soup.find_all("li", {"class": "item-block"})

     print('Stage 1')

     for post in posts:
        print('Stage 2')
        
        Lot = post.find(class_='auc-lot-link').get_text().replace('\n', '')
        print(Lot)

        Bid = post.find(class_='list-cols info-col-mobile').get_text().replace('\n', '')
        print(Bid)

        Title = post.find(class_='yaaa').get_text().replace('\n', '')
        print(Title)

        Info = post.find('a', class_='yaaa')['href']
        print(Info)

        Photo = post.find('img')['src']
        print(Photo)

        csv_writer.writerow([Lot, Bid, Title, Info, Photo])
print('Stage 3')

#