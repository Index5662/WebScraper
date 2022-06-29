


# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time

i=0

while i <= 0:                  #change 0 to number of loops you want +1 and pages to go through
 i = i + 1   
 time.sleep(1)              #time delay in seconds


 response = requests.get("https://www.dotmed.com/auctions/featured/10401367.html")              #link to direct bids auction
 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("div", {"class": "upcoming-auction"})
 
 print('Stage 1')

 filename = str(uuid.uuid4())
 print(filename)

 with open('Test' + filename + '.csv', 'w' ) as csv_file:                #file name
     csv_writer = writer(csv_file)
     headers = ['Lot', 'Bid', 'Title', 'Info', 'Photo']
     csv_writer.writerow(headers)
     
     print('WHY')
     
     for post in posts:
        print('Stage 3')

        #Lot = post.find(class_='left-container col-md-8')['h4']
        #print(Lot)

        Lot = post.find_all(class_= 'left-container col-md-8', attrs={'h4'})[0].get_text().strip()

        div = soup.find_all("div", class_ ="events-sub-list").h4
        get_2021 =[p.text for p in div if "2021" in p]

        #Bid = post.find('h3')['text']
        #print(Bid)

        #Title = post.find('h3')['text']
        #print(Title)

        #Info = post.find('h3')['href']
        #print(Info)

        #Photo = post.find(class_='link-container').get_text().replace('\n', '')
        #print(Photo)
        
        print('SOS')

        csv_writer.writerow([Lot,  ])
     print('Fu')
#There is no Asking Bid """Bid, Title, Info,Photo"""