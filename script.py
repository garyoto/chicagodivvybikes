import json
import urllib2

#get the 300 stations from divvy in json format
url = http://divvybikes.com/stations/json 

#load json data
d = json.load(urllib2.urlopen(url))

#extract the station list from original jason data
newd = d['stationBeanList'][1:]


#create new dict
ndict = {}

#add stationlist to dict
ndict['feature'] = newd

#add geojson metadata
ndict['type'] = 'FeatureCollection'



gj = open('divvybikestations.json', 'w')
newdata = json.dumps(ndict, indent=4)
gj.write(newdata)
gj.close()

