# google static maps api call -- returns a 640x640 image of a map

import requests
from url_signer import sign_url
from urllib.parse import urlencode


def get_map_image(polyline, max_north, max_east, max_west, max_south, api_key, secret):
    # api url for google static maps
    base_url = f"https://maps.googleapis.com/maps/api/staticmap"

    # find path center point
    mid_latitude = (max_north + max_south) / 2
    mid_longitude = (max_east + max_west) / 2

    # create northeast and southwest point strings
    northeast = f"{max_north},{max_east}"
    southwest = f"{max_south},{max_west}"

    # set api call parameters
    params = {
        "center": f"{mid_latitude},{mid_longitude}",
        "path": f"weight:4|color:0x0000FFFF|enc:{polyline}",
        "markers": f"{northeast}|{southwest}",
        "maptype": "satellite",
        "size": "640x640",
        "scale": 2,
        "format": "png32",
        "key": api_key,
    }

    # do url encoding on special characters
    query_string = urlencode(params)

    # create the full api call
    url = f"{base_url}?{query_string}"

    # add signature to call
    call = sign_url(url, secret)

    # send it
    response = requests.get(call)

    # write image if successful
    if response.status_code == 200:
        with open('map.png', 'wb') as f:
            f.write(response.content)

    # return api call success/fail
    return response.status_code


if __name__ == '__main__':
    status = get_map_image(1.2,2.3,3.4,4.5, "key", "secret")
    print(status)