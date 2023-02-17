import urllib.request
import json
import csv

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

features = data["features"]
turkey_syria_quakes = [quake for quake in features if "Turkey" in quake["properties"]["place"] or "Syria" in quake["properties"]["place"]]

with open("turkey_syria_quakes.csv", mode="w", newline="") as csv_file:
    fieldnames = ["time", "place", "mag", "magType", "latitude", "longitude", "depth"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for quake in turkey_syria_quakes:
        properties = quake["properties"]
        writer.writerow({
            "time": properties["time"],
            "place": properties["place"],
            "mag": properties["mag"],
            "magType": properties["magType"],
            "latitude": quake["geometry"]["coordinates"][1],
            "longitude": quake["geometry"]["coordinates"][0],
            "depth": quake["geometry"]["coordinates"][2]


        })
