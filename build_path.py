# https://developers.google.com/maps/documentation/maps-static/start
# https://archive.journeynorth.org/tm/LongitudeIntro.html


import os
from dotenv import load_dotenv
from api_call import get_map_image
from gpx_parse import extract_gpx_to_lists


load_dotenv()

api_key = os.getenv('API_KEY')
secret = os.getenv('SECRET')

latitudes, longitudes, elevations, times = extract_gpx_to_lists(file_path="test_ride.gpx")

north = max(latitudes)
south = min(latitudes)
east = max(longitudes)
west = min(longitudes)

status = get_map_image(max_north=north, max_south=south, max_east=east, max_west=west, api_key=api_key, secret=secret)

print(status)