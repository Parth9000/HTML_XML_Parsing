
import requests
import pandas as pd


## Extracting Data from HTML page

page = requests.get("https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=newjersey")


page

# displaying the page content 
page.content


# importing beautiful soup library 

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())



table = soup.find(lambda tag: tag.name=='table') 
rows = table.findAll(lambda tag: tag.name=='tr')

print(rows)


# extracting the first table header names

table_rows = table.find_all('tr')

l2 = []
for tr in table_rows:
    td = tr.find_all('th')
    row = [tr.text for tr in td]
    l2.append(row)

print(l2)


# extracting the first table rows and its content

table_rows = table.find_all('tr')

l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)

# creating the dataframe and storing our contents in it
l1=pd.DataFrame(l,columns=l2[0])
print(l1)


## Extracting Data from XML page

from bs4 import BeautifulSoup
import urllib.request
webpage = urllib.request.urlopen('https://data.lacity.org/api/views/nxs9-385f/rows.xml?accessType=DOWNLOAD')

soup1 = BeautifulSoup(webpage,'lxml')


print(soup1.prettify())


# Extracting relevant columns

zip_code=soup1.find_all('zip_code')
total_males=soup1.find_all('total_males')
total_females=soup1.find_all('total_females')


# creating empty lists

l3=[]
col1=[]
col2=[]
col3=[]


# extracting text data from the objects and storing in the lists

for tr3 in zip_code:
    col1.append(tr3.text)
for tr3 in total_males:
    col2.append(tr3.text)
for tr3 in total_females:
    col3.append(tr3.text)


# creating the dataframe to store our data
import numpy as np
l3=pd.DataFrame(np.column_stack([col1, col2, col3]),columns=['zip_code', 'total_males', 'total_females'])


print(l3)




