#downloads latest json data from divvybikes.com and make a geojson file out of it.

import json
import urllib2


url = 'http://divvybikes.com/stations/json'
features = []
d = json.load(urllib2.urlopen(url))
for idx, station in enumerate(d['stationBeanList']):
    # avoid first entry
    if idx:
        features.append({'type': 'Feature', 
                         'properties': station,
                         'geometry': {'type': 'Point',
                                      'coordinates': [station['longitude'], 
                                                      station['latitude']]}})

result = {'type': 'FeatureCollection', 'features': features}

gj = open('divvybikestations.geojson', 'w')
newdata = json.dumps(result, indent=4)
gj.write(newdata)
gj.close()

