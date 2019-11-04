# strava_createPolylines.py
# This python script is a simply loops through all of the cached Strava activities and extracts
# polylines. These are then stored in a .csv file.
#
# Chris Hughes 01/11/2019

import os
import csv
import json
import glob
from datetime import datetime

#Open the specific user variables
with open('data.json') as f:
    data = json.load(f)


os.path.exists(data['outputdir']) or os.makedirs(data['outputdir'])
with open("polylines.csv", "w") as runs_file:
	writer = csv.writer(runs_file, delimiter=",")

	for fn in sorted(glob.glob(data['outputdir'] + '/*_activity.json')):
		with open(fn) as f:
			print fn
			activity = json.load(f)
			if ("map" in activity):
				polyline = activity["map"]["polyline"]
				writer.writerow([activity["id"], polyline, activity['type'], datetime.strptime( activity['start_date_local'], '%Y-%m-%dT%H:%M:%S%fZ').strftime('%Y-%m-%d'), activity["average_speed"], activity["name"].encode("utf8")])
				
