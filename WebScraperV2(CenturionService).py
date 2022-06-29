




# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time


i=11
while i >= 10:
 time.sleep(10)
 

 response = requests.get("https://bid.centurionservice.com/auctions/catalog/id/371")


 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("li", {"class": "item-block"})

 filename = str(uuid.uuid4())

 with open('Auction372;' + filename + '.csv', 'w' ) as csv_file: 
     csv_writer = writer(csv_file)
     headers = ['Lot', 'Info', 'Photo', 'Bid', 'Asking', 'Title']
     csv_writer.writerow(headers)

     for post in posts:
        print('yup')

        Lot = post.find(class_='auc-lot-link').get_text().replace('\n', '')
        print(Lot)

        Info = post.find('a')['href']
        print(Info)

        Photo = post.find('img')['src']
        print(Photo)

        Bid = post.find(class_='value').get_text().replace('\n', '')
        print(Bid)

        Asking = post.find(class_='item-askingbid').get_text().replace('\n', '')
        print(Asking)

        Title = post.find(class_='yaaa').get_text().replace('\n', '')
        print(Title)
        
        csv_writer.writerow([Lot, Info, Photo, Bid, Asking, Title])








