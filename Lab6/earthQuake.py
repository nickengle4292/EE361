import urllib.request
import json
import csv
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson", context=context) as response:
    data = response.read()

earthquakes = []

for feature in json.loads(data)['features']:
    place = feature['properties']['place']
    if "Turkey" in place or "Syria" in place:
        time = feature['properties']['time']
        mag = feature['properties']['mag']
        magType = feature['properties']['magType']
        latitude = feature['geometry']['coordinates'][1]
        longitude = feature['geometry']['coordinates'][0]
        depth = feature['geometry']['coordinates'][2]
        earthquakes.append((time, place, mag, magType, latitude, longitude, depth))

with open('turkey_syria_earthquakes.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['time', 'place', 'mag', 'magType', 'latitude', 'longitude', 'depth'])
    writer.writerows(earthquakes)

