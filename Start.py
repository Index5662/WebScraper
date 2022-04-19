"""
from urllib.request import urlopen
url = "https://bid.centurionservice.com/auctions/catalog/id/365"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

title_index = html.find("<title>")
title_index

start_index = title_index + len("<title>")
start_index

end_index = html.find("</title>")
end_index

title = html[start_index:end_index]
title
"""














"""
from urllib.request import urlopen
url = "https://bid.centurionservice.com/auctions/catalog/id/365"
page = urlopen(url)

html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title

print(html)

import re
re.findall("ab*c", "ac")
"""











"""7/10
import re
from urllib.request import urlopen

url = "https://bid.centurionservice.com/auctions/catalog/id/365"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
"""

















"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://bid.centurionservice.com/auctions/catalog/id/365?view=list"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

soup.title
soup.title.string

soup.find_all("img")
"""











"""
import requests
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://bid.centurionservice.com/auctions/catalog/id/365?view=list") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    print(item['src'])
"""





















"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
  
htmldata = urlopen('https://bid.centurionservice.com/auctions/catalog/id/365?view=list')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')


for item in images:
    print(item['src'])


import re
from urllib.request import urlopen

url = "https://bid.centurionservice.com/auctions/catalog/id/365"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)

"""




















"""
from re import findall
import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://bid.centurionservice.com/auctions/catalog/id/365"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div', findall attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
"""























"""

from bs4 import BeautifulSoup
import requests
import os 
import os.path
import csv 
import time 


def writerows(rows, filename):
    with open(filename, 'a', encoding='utf-8') as toWrite:
        writer = csv.writer(toWrite)
        writer.writerows(rows)
 

def getlistings(listingurl):
    '''
    scrap footballer data from the page and write to CSV
    '''

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        response = requests.get(listingurl, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    soup = BeautifulSoup(response.text, "html.parser")

    listings = []

    # loop through the table, get data from the columns
    for rows in soup.find_all("tr"):
        if ("oddrow" in rows["class"]) or ("evenrow" in rows["class"]):          
                        
            name = rows.find("div", class_="name").a.get_text()
            hometown = rows.find_all("td")[1].get_text()
            school = hometown[hometown.find(",")+4:]
            city = hometown[:hometown.find(",")+4]
            position = rows.find_all("td")[2].get_text()
            grade = rows.find_all("td")[4].get_text()

            # append data to the list
            listings.append([name, school, city, position, grade])

    return listings


if __name__ == "__main__":
    '''
    Set CSV file name. 
    Remove if file alreay exists to ensure a fresh start
    '''
    filename = "footballers.csv"
    if os.path.exists(filename):
        os.remove(filename)
    
    '''
    Url to fetch consists of 3 parts:
    baseurl, page number, year, remaining url
    '''
    baseurl = "https://bid.centurionservice.com/" 
    page = 1
    parturl = "auctions/catalog/id/365"

    # scrap all pages
    while page < 259:
        listingurl = baseurl + str(page) + parturl
        listings = getlistings(listingurl)

        # write to CSV        
        writerows(listings, filename)

        # take a break
        time.sleep(3)

        page += 1

if page > 1:
    print("Listings fetched successfully.")


"""






















"""

import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://bid.centurionservice.com/auctions/catalog/id/365'

# opening url and grabbing the web page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')

# grabbing all containers with class name = item-container
containers = page_soup.findAll('div', {'class':'item-container'})

filename = "products.csv"
f = open(filename, 'w')

headers = "brands, product_name, shipping\n"

f.write(headers)

container = containers[1]

for container in containers:
    brand = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class':'item-title'})
    product_name = title_container[0].text
    ship_container = container.findAll('li', {'class':'price-ship'})
    # use strip() to remove blank spaces before and after text
    shipping = ship_container[0].text.strip()

    print("brand:" + brand)
    print("product_name:" + product_name)
    print("shipping:" + shipping)

    f.write(brand + ',' + product_name.replace(',' , '|') + ',' + shipping + '\n')

f.close()



"""














from bs4 import BeautifulSoup
import urllib
from urllib import request
import urllib.request as ur

# Getting input for webiste from user
urlinput = input("Enter url :https://bid.centurionservice.com/auctions/catalog/id/365")
print("https://bid.centurionservice.com/auctions/catalog/id/365", urlinput)

# For extracting specific tags from webpage
def getTags(tag):
  s = ur.urlopen(urlinput)
  soup = BeautifulSoup(s.read())
  return soup.findAll(tag)

# For extracting specific title & meta description from webpage
def titleandmetaTags():
    s = ur.urlopen(urlinput)
    soup = BeautifulSoup(s.read())
    #----- Extracting Title from website ------#
    title = soup.title.string
    print ('Website Title is :', title)
    #-----  Extracting Meta description from website ------#
    meta_description = soup.find_all('meta')
    for tag in meta_description:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            #print ('NAME    :',tag.attrs['name'].lower())
            print ('CONTENT :',tag.attrs['content'])

#------------- Main ---------------#
if __name__ == '__main__':
  titleandmetaTags()
  tags = getTags('h1')
  for tag in tags:
     print(tag) # display tags 
     print(tag.contents) # display contents of the tags



























"""
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://bid.centurionservice.com/auctions/catalog/id/365').read()


# In[2]:

soup = bs.BeautifulSoup(source,'html5lib')


# In[3]:

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)


# In[4]:

print(soup.find_all('p'))


# In[5]:

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))


# In[6]:

for url in soup.find_all('a'):
    print(url.get('href'))


# In[9]:

nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))
          


# In[10]:

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)


# In[11]:

for div in soup.find_all('div', class_='body'):
    print(div.text)


# In[12]:

#scrapping specifically with a table example
table = soup.table

#find the table rows within the table
table_rows = table.find_all('tr')

# iterate through the rows, find the td tags, and then print out each of the table data tags:
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)


# In[14]:

soup = bs.BeautifulSoup(source,'xml')
for url in soup.find_all('loc'):
    print(url.text)


# In[15]:

soup = bs.BeautifulSoup(source,'lxml')

js_test = soup.find('p', class_='jstest')

print(js_test.text)


# In[18]:

print("it will be contunued")


# In[ ]:
"""



















"""
from bs4 import BeautifulSoup
import requests

headers={
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65."
}
r=requests.get("https://bid.centurionservice.com/auctions/catalog/id/365",headers=headers)

# Printing some response text
print(r.text[:500])

soup=BeautifulSoup(r.content)

count=0
College_name=[]
location=[]
ratings=[]
other_details=[]
for section in soup.findAll('section', attrs={"class":'ctp_container'}):
    college= section.findAll('div',attrs={'class':"ctpSrp-tuple"})
    
#     rating= find('span',attrs={'class':'rating-block rvw-lyr'})
    
#     print(college.text)
    for c in college:
        count= count+1
        name=c.find('p', attrs={"class":"ctpIns-tl"})
        College_name.append(name.text)
        print(name.text)
        loc=c.find('p', attrs={"class":"ctp-cty"})
        print(loc.text)
        location.append(loc.text)
        
        rating=c.find('span', attrs={"class":"rating-block rvw-lyr"})
        ratings.append(rating.text)
        print(rating.text)
        d=c.find('div', attrs={"class":"ctp-detail"})
        other_details.append(d.text)
        print(d.text)
#         div=c.find('div',attrs={"class": "ctpSrp-Lft"})
#         s=div.find('img')
#         print(s.attrs['src'])



<ipython-input-5-4d9e6cf83ac5> in <module>()
rating=c.find('span', attrs={"class":"rating-block rvw-lyr"})
ratings.append(rating.text)
print(rating.text)
d=c.find('div', attrs={"class":"ctp-detail"})



print(count)
print(len(College_name))
print(len(location))
print(len(ratings))
print(len(other_details))
del College_name[-1]
del location[-1]


import pandas as pd
data=pd.DataFrame({
           'Institution_Name':College_name,
           'Location': location,
           'Ratings':ratings,
           'other_details':other_details
    
}, columns = ['Institution_Name','Location','Ratings','other_details'])
# print(data.info)
print(data.head())
data.to_csv('Main.csv', sep='\t', encoding='utf-8')


for section in soup.findAll('section', attrs={"class":'ctp_container'}):
#     print(section)
    college= section.find('div',attrs={'class':"ctpSrp-tuple"})
    div=college.find('div',attrs={"class": "ctp-SrpDiv"})
    print(div)
    s=div.findAll('img')
    print(s)
#     print(college)
    
 
"""











"""
#!/usr/bin/env python
# coding: utf-8

#Requirements
#pip3 install requests
#pip3 install bs4

#run in the browser also what are you doing with the help of chrome driver

# ## Basic fundamentals of web scraping

# import these two modules bs4 for selecting HTML tags easily
from bs4 import BeautifulSoup
# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests
from selenium import webdriver

# I put here my own blog url ,you can change it.
url="https://bid.centurionservice.com/auctions/catalog/id/365"
BASE_URL = "https://bid.centurionservice.com"
#Requests module use to data from given url
source=requests.get(url)


def get_chrome_web_driver(options):
    return webdriver.Chrome("./chromedriver", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')

# BeautifulSoup is used for getting HTML structure from requests response.(craete your soup)
soup=BeautifulSoup(source.text,'html')

# Find function is used to find a single element if there are more than once it always returns the first element.
title=soup.find('title') # place your html tagg in parentheses that you want to find from html.
print("this is with html tags :",title)

qwery=soup.find('h1') # here i find first h1 tagg in my website using find operation.

#use .text for extract only text without any html tags
print("this is without html tags:",qwery.text) 


links=soup.find('a') #i extarcted link using "a" tag
print(links)


# ## extarct data from innerhtml 

# here i extarcted href data from anchor tag.
print(links['href']) 

##  or another way
##extracting href(links) attribute and anchor(<a>) tag from page 
for a in soup.find_all('a', href=True):
    print ( a['href'])

for i in links:
    print(i.text)

# similarly i got class details from a anchor tag
print(links['class'])


# ## findall operation in Bs4

# findall function is used to fetch all tags at a single time.
many_link=soup.find_all('a') # here i extracted all the anchor tags of my website
total_links=len(many_link) # len function is use to calculate length of your array
print("total links in my website :",total_links)
print()
for i in many_link[:6]: # here i use slicing to fetch only first 6 links from rest of them.
    print(i)

second_link=many_link[1] #here i fetch second link which place on 1 index number in many_links.
print(second_link)
print()
print("href is :",second_link['href']) #only href link is extracted from ancor tag


# select div tag from second link
nested_div=second_link.find('div')
# As you can see div element extarcted , it also have inner elements
print(nested_div)
print()
#here i extracted class element from div but it give us in the form of list
z=(nested_div['class'])
print(z)
print(type(z))
print()
#  " " .join () method use to convert list type  into string type
print("class name of div is :"," ".join(nested_div['class'])) 


# ## scrap data from wikipedia

wiki=requests.get("https://bid.centurionservice.com/auctions/catalog/id/365")
soup=BeautifulSoup(wiki.text,'html')
print(soup.find('title'))


# ### find html tags with classes

ww2_contents=soup.find_all("div",class_='toc')
for i in ww2_contents:
    print(i.text)


overview=soup.find_all('table',class_='infobox vevent')
for z in overview:
    print(z.text)
  
images=soup.find_all('img')

images
##or
print(images)

"""





"""

import requests
import bs4
import re
#imported the modules I will require in the project

#http://en.wikipedia.org/wiki/Member_states_of_the_United_Nations - The wikipedia page I'm scraping

root_url = 'https://bid.centurionservice.com/auctions/catalog/id/365'
page_url = root_url + '/wiki/Member_states_of_the_United_Nations' 

r = requests.get(page_url) #returns the HTML of the page, can be done through urlopen as well
#The HTML of the website formed by the url is retrieved by the get function and stored in r


#Then we use the python library BeautifulSoup to parse the HTML code, by creating a soup of the contents of the retrieved HTML codes of the webpage
soup = bs4.BeautifulSoup(r.content)

#print soup
#for link in soup.find_all("a"):
#    print link.get("href")


fp=open('data_wiki.txt','w+')
#An empty file created for the purpose of storing data from our source page; data_wiki.txt stores general information from the chosen Wiki page, i.e the member countries in the UN. Along with that, it lists the countries about which we will be scraping more info from the respective links


fp.write( soup.select('div p')[0].get_text() + '\n')
#Writing general info about the UN and the member nations on to the file
fp.write( soup.select('div p')[4].get_text() + '\n\n')
#select function is used to retrieve the required HTML tag. It returns the whole HTML line complete with the tags

#The returned HTML code is the code made up by the first <p> tag (because of [0]), and the fifth <p> tag (as specified using [5]) under the> <div> tag.
#Using get_text, we retrieve the textual information contained between the text, the actual text that shows up on the website

country=[] #List variable used to iterate over the country names
countries=[]    #List of all the 10 chosen countries 
admission_date=[]   #Date of admission of the country into the UN

fp.write('%-15s  %-15s\n\n' %('Country', 'Admission_date'))
#Headers for the file

for i in range(11,21):
 
    country= (str( soup.select('tr a[href^=/wiki]')[i].get_text() ) ) 
    #Again,select function is used to retrieve the required HTML tag. It returns the whole HTML line wherever it finds an anchor tag beginning with /wiki, like <a href="/wiki...whatever">, under the base tag tr.
    #This piece of code makes the tag 'country' point to the parsed country which is assigned to it

    countries.append((str( soup.select('tr a[href^=/wiki]')[i].get_text() ) )) #Adding country name to the list
    
    admission_date = ( str(soup.select('tr span[style^="white"]')[i-3].get_text() ))
    #Similarly, this piece of code parses the date of admission of the country and assigns it to admission date. 
    #The HTML code of the admission date carries the tag <span style=/wiki...something..>, which is the information I have exploited to extract the required date.
    
    
    fp.write('%-15s  %-15s\n' %(country, admission_date))
    #This data about a country and its date of admission is then written into the file with the appropriate formatting.
    
fp.write('\n\n')

fp.write( str(soup.select('ul li[id^="footer"]')[0].get_text() ).strip(' ') + '\n\n')
#Along with that, the last date of modification of the webpage is extracted from the footer. It is contained as a text inside the li tag, which itself lies inside the ul tag in the HTML of the page.
#It is converted into a string and stripped of all formatting before it is added to the file using fp.write(). 

fp.write( 'Now let us find some basic information about these countries from their Wikipedia page, using a Python script') 

fp.close() #Closed the file for the source page data

#Empty list for storing the page urls of the countries, who's wikipedia page I have to parse next
urls = []



   #print (link.get("href"))
'''   
for link in soup.select('tr')[2]:
   print link.find('a').attrs['href']   
'''
  
i=1 #intitalised a counter variable which counts from 1 to 10

for link in soup.select('tr a[href^=/wiki]'):
    #for link in soup.find_all('a'):
    if(i>11 and i<=21):  #A chunk of 10 urls belonging to 10 different countries is extracted somehwere from the middle of the list of countries displayed on the source web page.
    
        urls.append(str(link.get('href')) ) #Add the page url to the list
    i=i+1   #Increment counter
   
   #soup.select('div#sidebar a[href^=http://www.youtube.com]')[0].get_text()
 
#mw-content-text > table.sortable.wikitable.jquery-tablesorter


#Another empty file for writing the information extracted from the page of every country we traverse.
fp = open('data_from_links.txt','w+')  #The file has been opened in write mode using w+

fp.write('%-12s  %-12s %-20s %-15s %-25s %-15s %-25s\n\n' %(' ',  'Capital' ,'Official Language', 'Telephone Code', 'President', 'Demonym ', 'Page Last Modified')) 
#Headers for the information to be stored about each country


#Empty lists, to which the associated attributes of each country will be assigned
language = []
capital = []
telephone = []
presidents = []
demonym = []
modified = []

for i in range(len(urls)):  #for loop begins; We iterate over all the page urls in our list urls[]

    r = requests.get(root_url + urls[i])
    soup = bs4.BeautifulSoup(r.text)
    #Just like I did before, now I will parse the HTML code of each of the countries pages one by one, by cooking a separate soup for each of them, to retrieve their HTML code
    
    
    #Retrieving the Official LANGUAGE of each country 
    if i==5:
        language = (str(soup.select('div#bodyContent tr td')[10].get_text() ))
    else:
        language = ( str( soup.select('div#bodyContent tr a[href$=language]')[0].get_text() ))
        
     #Needed to access a separate set of tags for one particular country. That is how the HTML of the webpage was written,
     #For all other countries, I was able to extract info from the <tr..> tag where href ends with the word language
     
     #NOTE: The $ symbol here denotes a regular expression, wherein we are matching our required info with the characters at the end of something. So ony those href tags in the code which end at 'language' are selected
        
        
    #Code used to retrieve the capital of each country    
    if (i==4 or i==7 or i==8 or i==9):
        capital = ( str( soup.select('div#bodyContent tr[class^=mergedtoprow] td a[href^=/wiki]')[5].get_text() ) )    
    else:
        capital = ( str( soup.select('div#bodyContent tr[class^=mergedtoprow] td a[href^=/wiki]')[4].get_text() ) )
    
    # The HTML of the pages is such that all the capital names are not contained in the same tag.
    #Therefore, I had to retrieve the capital names from different tags for different countries
    
    #NOTE: The data recieved in unicode format is first converted into a string, and then stripped of any formatting so that it can successfully written to the file
    
    #Retrieving the telephone code of the country
    if (i==2 or i==5 ):
        telephone = ( str( soup.select('div#bodyContent tr td a[href^=/wiki/Area]')[0].get_text() ))
    elif(i==6 or i==9):
        telephone = ( str( soup.select('div#bodyContent tr td a[href^=/wiki/%2B]')[0].get_text() ))
    elif(i==8):
        telephone = (' ')
    else:
        telephone = ( str( soup.select('div#bodyContent tr td a[href^=/wiki/Telephone]')[0].get_text() ))
     #Had to retrieve the capital names from different tags for different countries due to inconsistencies in the page HTML codes
        

    
    #Retrieving the names of the incumbent presidents for each country
    if i==9:
        presidents = ( str( soup.select('div#bodyContent tr[class^=mergedbottomrow] td a[href^=/wiki/]')[2].get_text() ) )
    else:
        presidents = ( str( soup.select('div#bodyContent tr[class^=mergedrow] td a[href^=/wiki/]')[1].get_text()  ) )     
    
    
    #Retrieving the demonym with which the people of each country are referred to, and then assigned to the list demonym.
    #It again lies at different places for different countries.
    if (i==0 or i==1 or i==3 or i==7):
        demonym = ( str( soup.select('div#bodyContent tr td a[class^=mw-redirect]')[1].get_text() ))
    elif (i==2 or i==5 or i==8):
        demonym = ( str( soup.select('div#bodyContent tr td a[class^=mw-redirect]')[3].get_text()   ) )
    elif (i==4):
        demonym = ( str( soup.select('div#bodyContent tr td a[class^=mw-redirect]')[2].get_text() ) )
    elif (i==6):
        demonym = ( str( soup.select('div#bodyContent tr td a[href^=/wiki/Belarusian]')[1].get_text() ) )
    else:
        demonym = (str( soup.select('div#bodyContent tr td ul li')[16].get_text() ))
       
    
    #The list modified is assigned the date and time of the latest modification of the wikipedia page of the respective countries
    modified = ( str(soup.select('ul li[id^="footer"]')[0].get_text() ).strip(" This page was last modified on") )
     
    #THE DATA WRITING STEP
    fp.write('%-12s  %-12s %-20s %-15s %-25s %-15s %-25s\n' %(countries[i],  capital, language, telephone, presidents, demonym, modified))    
  
#All data generated is written to the file while taking care to left align every data element for consitency and ease of removal of a value from the file. '-' sign signifies the left alignment  
    #The write attributes %-12s , %-12s, %-15s,  etc tell us the maximum space(length) the attributes in the respective columns can take
    #Here I have hard coded this data, keeping in mind the maximum values each attribute can take, otherwise we can also run a for loop and calculate the maxlength an attribute can take for each field.
     
    print(...)
    
fp.close() #closing the file 

"""










"""

# we import the class that we need scraping our blog

import requests
from bs4 import BeautifulSoup
from csv import writer


# we create a response variable

response = requests.get('https://bid.centurionservice.com/auctions/catalog/id/365')

# we initialize beautiful soup and pass in our response

soup = BeautifulSoup(response.text, 'html.parser')

# we create a variable called posts and we know that our all our blog posts are in a div called blog-entry-content

posts = soup.findAll(class_='blog-entry-content')


# writing to csv file

with open('articles.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)

    # creating headers in the csv file
    headers = ['Lot', 'Info', 'Photo']

    # writing a row of headers in the csv
    csv_writer.writerow(headers)

    # now lets loop through our posts

    for post in posts:
        Lot = post.find(class_='auc-lot-link')  #.get_text().replace('\n', '')
        Info = post.find(class_='yaaa')['href']
        Photo = post.select('src=')[0].get_text()
        csv_writer.writerow([Lot, Info, Photo])

"""








# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer
# we create a response variable
response = requests.get('https://bid.centurionservice.com/auctions/catalog/id/365?view=list&items=100')
# we initialize beautiful soup and pass in our response
#print(response.text);

soup = BeautifulSoup(response.text, 'html.parser')


# we create a variable called posts and we know that our all our blog posts are in a div called blog-entry-content
posts = soup.find_all("li", {"class": "item-block"})


# writing to csv file
with open('article2.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
 
    # creating headers in the csv file
    headers = ['Lot', 'Info', 'Photo', 'Bid', 'Title']
 
    # writing a row of headers in the csv
    csv_writer.writerow(headers)
    # now lets loop through our posts
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






















# basic scrape and write demonstration used in Goldsmiths digital sandbox 2014
import urllib		# fetches raw web pages for us
import bs4		# turns raw web pages into object hierarchy and provides selectors (like CSS and Xpath does)
import csv		# simplifies the process of writing data to Comma Separated Values in a file

# a list of URLs on YouTube that we want to scrape data from
pagesToScrape = ['https://bid.centurionservice.com/auctions/catalog/id/365'
				,'https://bid.centurionservice.com/auctions/catalog/id/365']

# open a file in append mode to write into in the same directory where we ran this script from
csvfile = open('tubedata.csv', 'a')
csvwriter = csv.writer(csvfile)

# loop over our list of URL's one at a time
for URL in pagesToScrape:

	webpage = urllib.urlopen(URL)			# fetch webpage
	soup = bs4.BeautifulSoup(webpage)		# make an object from the HTML

	# extract info from soup
	title = soup.find('span', {'id':'eow-title'}).string
	uploader = soup.find('div', {'class':'yt-user-info'}).a.string
	date = soup.find('div', {'id':'watch-uploader-info'}).strong.text[12:]

	# another way of using BS4 to select stuff
	views =  soup.find("div", class_="watch-view-count").string

	# views is a number with commas in it, lets make it a proper number by replacing the commas with nothing!
	views = int(views.replace(',', ''))

	# print info to screen, we can reomve excess white space around the title using the strip() function
	print 'title: ', title.strip()
	print 'uploader: ', uploader
	print 'date: ', date
	print 'views:' , views
	csvwriter.writerow([title.strip(), uploader, date, views])		# write a row in the file
	

# FURTHER EXERCISES
# ruggedise your script by using the python 'with' statement to open your file and the 'try-except' structure

