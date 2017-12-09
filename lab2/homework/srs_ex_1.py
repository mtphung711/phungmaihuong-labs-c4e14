from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

webpage = urlopen('https://www.apple.com/itunes/charts/songs/')
data = webpage.read()
html_content = data.decode('utf8')

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section', 'section chart-grid')
ul = section.find('ul')
li_list = ul.find_all('li')

top_100 = []

for li in li_list:
    h3 = li.h3
    a3 = h3.a
    h4 = li.h4
    a4 = h4.a
    songs = {
        'title': a3.string,
        'artist': a4.string
    }
    top_100.append(songs)

pyexcel.save_as(records=top_100, dest_file_name='itunes_chart.xlsx')

options = {
    'default_search': 'ytsearch',
    'max_downloads' : len(top_100),
    'format': 'bestaudio/audio'
}

dl = YoutubeDL(options)
for song in top_100:
    dl.download(['title' + 'artist'])
