#Tek Yard Web Scraper


#Import Plugins
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time
import os

i=0

while i <= 88:           #0 = number of loops +1  or  #0 = number of pages +1
 i = i + 1   
 print(i)
 time.sleep(720)

 
 response = requests.get("https://www.proxibid.com/reLink-Medical-Auctions-LLC/reLink-Medical-February-2022-Auction/event-catalog/208958?p=" + str(i))              #link to direct bids auction
 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("div", {"class": "grid-container fluid"})

 print('Stage 1')

 filename = str(uuid.uuid4())
 print(filename)

 with open('TekYard;' + filename + '.csv', 'w' ) as csv_file:                #file name
     csv_writer = writer(csv_file)
     headers = ['Filler']
     csv_writer.writerow(headers)

     for post in posts:
        print('Stage 2')

        Filler =1

        csv_writer.writerow([Filler])
print('Stage 3')






