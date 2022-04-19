"""
# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get("https://bid.centurionservice.com/auctions/catalog/id/370?page=1&items=100&view=list"
                       ,"https://bid.centurionservice.com/auctions/catalog/id/370?page=2&items=100&view=list" )



soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all("li", {"class": "item-block"})


with open('article2.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Lot', 'Info', 'Photo', 'Bid', 'Title']
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
        Title = post.find(class_='yaaa').get_text().replace('\n', '')
        print(Title)
        csv_writer.writerow([Lot, Info, Photo, Bid, Title])

"""





# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer


response = ("https://bid.centurionservice.com/auctions/catalog/id/370?page=1&items=100&view=list"
           ,"https://bid.centurionservice.com/auctions/catalog/id/370?page=2&items=100&view=list" )

for URL in response:
 requests.get

 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("li", {"class": "item-block"})


with open('article2.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Lot', 'Info', 'Photo', 'Bid', 'Title']
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
        Title = post.find(class_='yaaa').get_text().replace('\n', '')
        print(Title)
        csv_writer.writerow([Lot, Info, Photo, Bid, Title])
