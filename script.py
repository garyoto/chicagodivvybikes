import json
import urllib2

#get the 300 stations from divvy in json format
url = 'http://divvybikes.com/stations/json'

#load json data
d = json.load(urllib2.urlopen(url))

#extract the station list from original jason data
newd = d['stationBeanList'][1:]


#create new dict
ndict = {}
tdict = {}

#add stationlist to dict
ndict['features'] = newd

#add "properties"
ndict['properties'] = newd

#add "type": "Feature" to ndict
p = {'type': 'Feature'}
tdict = tdict.update(p)

#add geojson metadata
ndict['type'] = 'FeatureCollection'


#add "properties" as key to each nested dict


#add k:v pair "type": "Feature" to each nested dict

#Extract Latitude and Longitude from each bike station
#append "geometry" : { "type": "Point", "coordinates": [ xx.xxxxxxxxx, yy.yyyyyyyyyy  ] } to list

#output geojson file
gj = open('divvybikestations.geojson', 'w')
newdata = json.dumps(ndict, indent=4)
gj.write(newdata)
gj.close()

