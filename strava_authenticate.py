# strava_authenticate.py
# This python script is a simple guide to the steps for connecting to the Strava API and 
# getting the access and refresh tokens. It saves all of the user data into a .json file
#
# Chris Hughes 01/11/2019

import requests
import json

#Open Data
with open('data.json') as f:
    data = json.load(f)

print "1. Visit https://www.strava.com/settings/api and create an app."

#Get Client ID
data['client_id'] = raw_input("2. Enter your Client ID [" + data['client_id'] + "]: ") or data['client_id']

#Get Client Secret
data['client_secret'] = raw_input("3. Enter your Client Secret [" + data['client_secret'] + "]: ") or data['client_secret']

#Get Authorization Code
print "4. Please visit:"
print "https://www.strava.com/oauth/authorize?client_id=" + data['client_id'] + "&redirect_uri=http://localhost&response_type=code&scope=activity:read"
code = raw_input("Copy and Paste the code value from the from the URL that you are directed to: ") 

#Get Access Token and Refresh Token
r=requests.post("https://www.strava.com/oauth/token?client_id=" + data['client_id'] + "&client_secret=" + data['client_secret'] + "&code=" + code + "&grant_type=authorization_code")
response = r.json()
data['access_token'] = response['access_token']
data['refresh_token'] = response['refresh_token']

#Get Output Directory
data['outputdir'] = raw_input("5. Strava Cache Directory [stravaData]: ") or "stravaData"

#Write Data to file
with open('data.json', 'w') as f:
    json.dump(data, f)
    
print "6. Success"


