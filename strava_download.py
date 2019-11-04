import requests
import os
import sys
import json
import glob

#Get arguments from User
if (len(sys.argv) < 2):
	print "Please Supply an argument (all | lastpage)"
	sys.exit()
multiplePages = 0
if str(sys.argv[1]) == 'all':
	multiplePages = 1

#Open the specific user variables
with open('data.json') as f:
    data = json.load(f)

#Perform a test request to see if our access works
headers = {'Authorization': "Bearer {0}".format(data['access_token'])}
r = requests.get("https://www.strava.com/api/v3/athlete/activities?page={0}".format(1), headers = headers)
response = r.json()

#If there is an message then we assume it is an error, request a new token.
if 'message' in response:
	print "Refreshing Token"

	r=requests.post("https://www.strava.com/api/v3/oauth/token?client_id=" + data['client_id'] + "&client_secret=" + data['client_secret'] + "&refresh_token=" + data['refresh_token'] + "&grant_type=refresh_token")
	response = r.json()
	data['access_token'] = response['access_token']
	data['refresh_token'] = response['refresh_token']
	headers = {'Authorization': "Bearer {0}".format(data['access_token'])}
	
	with open('data.json', 'w') as f:
		json.dump(data, f)

#If the output directory doesn't exist create it
os.path.exists(data['outputdir']) or os.makedirs(data['outputdir'])

#Make a list of the existing files so we can avoid re-downloading files
got = []
for fn in glob.glob(data['outputdir'] + '/*.json'):
	got.append(fn)

#Loop through all activities and cache them to files
page = 1
while True:
	r = requests.get("https://www.strava.com/api/v3/athlete/activities?page={0}".format(page), headers = headers)
	response = r.json()
	#print response
	if len(response) == 0:
		break
	else:
		for activity in response:
			print activity["id"],
			if data['outputdir'] + '/' + str(activity["id"]) + '_activity.json' in got:
				print 'Exists'
			else:
				print 'Downloading'
				url = "https://www.strava.com/api/v3/activities/{0}?include_all_efforts=true".format(activity["id"])
				r = requests.get(url, headers = headers)
				with open(data['outputdir'] + '/' + str(activity["id"]) + '_activity.json', 'w') as outfile:
					json.dump(r.json(), outfile)

				url = "https://www.strava.com/api/v3/activities/{0}/streams?keys=distance,altitude,time,latlng,heartrate,velocity_smooth,grade_smooth&key_by_type=".format(activity["id"])
				r = requests.get(url, headers = headers)
				with open(data['outputdir'] + '/' + str(activity["id"]) + '_stream.json', 'w') as outfile:
					json.dump(r.json(), outfile)
		if (multiplePages == 0):
			break		
		page += 1


