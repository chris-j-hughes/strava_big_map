# strava_big_map
This is a simple set of python scripts which download your data from Strava, and generate a polyline map.
You can find an example of the end result at: www.chrisjhughes.co.uk/apps/bigmap

# Quick Guide
Place all files on a webserver (with php, python)

Run 'python strava_authenticate.py' and follow instructions:

1. Visit https://www.strava.com/settings/api and create an app, making note of your client_id and client_secret.
2. Enter your client_id as shown in the Strava app setting in the Strava website.
3. Enter your client_secret as shown in the Strava app setting in the Strava website.
4. Visit the URL as asked by the script in any browser. Strava will ask you to log in and authenticate the connection. Once you have authenticated it will redirect to a page which cannot load. In the URL of this new page is a code. Copy and paste this code into the terminal when asked.
5. Specify a directory fot the strava data to be stored in. By default this is 'stravaData'

Run 'python strava_download.py'. You must specify if you would like all of the data to be downloaded or just the last page, by specifying 'all' or 'lastpage'. Generally downloading all the data can take a while, so when just performing an update 'lastpage' is enough.

Run 'python strava_createPolylines.py'. This will create a polylines.csv which can be used by index.php to render a map.




# Example output:

chris@data:/var/www/html/apps/maptest$ python strava_authenticate.py 
1. Visit https://www.strava.com/settings/api and create an app.
2. Enter your Client ID []: xxxxx
3. Enter your Client Secret[: xxxxxxxxxxxxxxxxxxxxxxxxx
4. Please visit:
https://www.strava.com/oauth/authorize?client_id=13596&redirect_uri=http://localhost&response_type=code&scope=activity:read
Copy and Paste the code value from the from the URL that you are directed to: xxxxxxxxxxxxxxxxxxxxxxxxx
5. Strava Cache Directory [stravaData]: 
6. Success


chris@data:/var/www/html/apps/maptest$ python strava_download.py all
2832573651 Downloading
2822359632 Downloading
2820217519 Downloading
2818865392 Downloading
2816277694 Downloading
2811899364 Downloading
2806344806 Downloading
2804889771 Downloading
2798585581 Downloading
2795322576 Downloading
2785089664 Downloading
2778943721 Downloading
2768497343 Downloading
2768234362 Downloading
2763048281 Downloading
2754320867 Downloading
2749921404 Downloading
2742066820 Downloading
2731331227 Downloading
2731329584 Downloading
2691547798 Downloading
2663656004 Downloading
2648824161 Downloading
2640266960 Downloading
2568735292 Downloading
2568732865 Downloading
2545512852 Downloading
2529677727 Downloading
2521322918 Downloading
2508787515 Downloading


chris@data:/var/www/html/apps/maptest$ python strava_createPolylines.py 
stravaData/2508787515_activity.json
stravaData/2521322918_activity.json
stravaData/2529677727_activity.json
stravaData/2545512852_activity.json
stravaData/2568732865_activity.json
stravaData/2568735292_activity.json
stravaData/2640266960_activity.json
stravaData/2648824161_activity.json
stravaData/2663656004_activity.json
stravaData/2691547798_activity.json
stravaData/2731329584_activity.json
stravaData/2731331227_activity.json
stravaData/2742066820_activity.json
stravaData/2749921404_activity.json
stravaData/2754320867_activity.json
stravaData/2763048281_activity.json
stravaData/2768234362_activity.json
stravaData/2768497343_activity.json
stravaData/2778943721_activity.json
stravaData/2785089664_activity.json
stravaData/2795322576_activity.json
stravaData/2798585581_activity.json
stravaData/2804889771_activity.json
stravaData/2806344806_activity.json
stravaData/2811899364_activity.json
stravaData/2816277694_activity.json
stravaData/2818865392_activity.json
stravaData/2820217519_activity.json
stravaData/2822359632_activity.json
stravaData/2832573651_activity.json
