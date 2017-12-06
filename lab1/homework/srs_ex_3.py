from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')

db = client.get_default_database()

customers = db['customers']

wom = customers.find({"ref": "wom"}).count()
ads = customers.find({"ref": "ads"}).count()
events = customers.find({"ref": "events"}).count()

print('''Word of mouth : {0}
Events : {1}
Ads : {2}'''.format(wom, ads, events))

from matplotlib import pyplot

labels = ['WOM', 'ADS', 'EVENTS']
colors = ['#f993f1', '#76d7e0', '#e5ed50']
data = [wom, ads, events]
pyplot.pie(data, labels=labels, colors=colors, autopct='%1.0f%%')
pyplot.axis('equal')
pyplot.show()
