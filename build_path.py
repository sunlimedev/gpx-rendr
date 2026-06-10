# https://developers.google.com/maps/documentation/maps-static/start
# https://archive.journeynorth.org/tm/LongitudeIntro.html

import os
import polyline
from PIL import Image
from dotenv import load_dotenv
from api_call import get_map_image
from gpx_parse import extract_gpx_to_lists

# load environment file
load_dotenv()

# load environment variables
api_key = os.getenv('API_KEY')
secret = os.getenv('SECRET')

# get gps data from gpx file
latitudes, longitudes, elevations, times = extract_gpx_to_lists(file_path="test_ride.gpx")

# find maximum values
north = max(latitudes)
south = min(latitudes)
east = max(longitudes)
west = min(longitudes)

# find start and finish points
start_latitude = latitudes[0]
start_longitude = longitudes[0]
finish_latitude = latitudes[-1]
finish_longitude = longitudes[-1]

# create ordered pairs
coordinates = list(zip(latitudes,longitudes))

# create polyline
polyline = polyline.encode(coordinates)

# do api call
status = get_map_image(polyline=polyline,
                       start_latitude=start_latitude,
                       start_longitude=start_longitude,
                       finish_latitude=finish_latitude,
                       finish_longitude=finish_longitude,
                       max_north=north,
                       max_south=south,
                       max_east=east,
                       max_west=west,
                       api_key=api_key,
                       secret=secret)

# crop image if call was successful
if status == 200:
    # print status
    print('Success')

    # open the map image
    img = Image.open('call_result.png')

    # get the image dimensions
    width, height = img.size

    # remove outer margins
    crop_box = (40, 35, width - 40, height - 45)

    # perform the crop
    cropped_img = img.crop(crop_box)

    # save the image
    cropped_img.save('map.png')