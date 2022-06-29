import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time
from datetime import datetime

Day = int(0)        #How Long Till Program Starts
Hour = int(0)
Minute = int(0)
Second = int(0)

DelayMinute = int(0)        #How Long Between Beggining and End of Page of Lots
DelaySecond = int(0)

NumberOfLoops = int(1)      #Number of Pages

Link = str("https://auctions.britishmedicalauctions.co.uk/auctions/catalog/id/521/June-2022-Endoscopy-Part-2")      #Link

#-------------------------------------------------------------------------------------------------------------------

DelaySecond1 = DelayMinute*60
DelayTime = (DelaySecond1+DelaySecond)

Hour1 = Day*24
Minute1 = (Hour1+Hour)*60
Second1 = (Minute1+Minute)*60
timedelay1 = (Second1+Second)
timedelay = (timedelay1-DelayTime)

LoopNumber = (NumberOfLoops-1)

i=0
time.sleep(timedelay)

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = str(timestr)
print(filename)

with open('BritishMedicalAuctions;' + filename + '.csv', 'w' ) as csv_file:
 headers = ['Lot', 'Bid', 'Title', 'Info', 'Photo']
 csv_writer = writer(csv_file)   
 csv_writer.writerow(headers)

 while i <= LoopNumber:                  #change 0 to number of loops you want +1 and pages to go through
     i = i + 1   
     print(i)
     time.sleep(DelayTime)              #time delay in seconds

     response = requests.get(Link + str(i))              #link to direct bids auction
     soup = BeautifulSoup(response.text, 'html.parser')
     posts = soup.find_all("li", {"class": "item-block"})

     for post in posts:
        
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

