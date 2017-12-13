from urllib.request import urlopen
from bs4 import BeautifulSoup #Camel Case

# 1. Download dantri
webpage = urlopen('http://dantri.com.vn') #Open a connection
data = webpage.read()
html_content = data.decode('utf8')


# 2. Analyze ROI (Region of Interest)
# 2.1 Create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'ul1 ulnew') # find one, find chi tim dc chieu tu tren xuong
li_list = ul.find_all('li')
# print(li_list[0].prettify())

# li = li_list[0]

news_list = []

for li in li_list:
    h4 = li.h4 # find('h4')

    a = h4.a # find('a')
    # print(a.string)
    news = {                    # de title va link luon di vs nhau
        'title': a.string,
        'link': 'http://dantri.com.vn' + a['href']
    }
    news_list.append(news)

import pyexcel

pyexcel.save_as(records=news_list, dest_file_name='dantri.xlsx')



# 3. Extract data from ROI
