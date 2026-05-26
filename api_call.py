# https://developers.google.com/maps/documentation/maps-static/start
# https://archive.journeynorth.org/tm/LongitudeIntro.html
# need to center it on the gpx path, then include northeast and southwest maximums as visible parameter, possibly add start marker and end marker

import os
import requests
from dotenv import load_dotenv
from urlsigner import sign_url

load_dotenv()

api_key = os.getenv('API_KEY')
secret = os.getenv('SECRET')

parameters = "size=640x640&zoom=16&center=belleisle,richmond&maptype=satellite"

url = (f"https://maps.googleapis.com/maps/api/staticmap?{parameters}&key={api_key}")

call = sign_url(url, secret)

response = requests.get(call)

if response.status_code == 200:
    print(response)
    with open('local_image.jpg', 'wb') as f:
        f.write(response.content)