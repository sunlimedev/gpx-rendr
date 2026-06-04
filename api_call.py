# google static maps api call -- returns a 640x640 image of a map


import requests
from url_signer import sign_url


def get_map_image(max_north, max_east, max_west, max_south, api_key, secret):
    base_url = f"https://maps.googleapis.com/maps/api/staticmap"

    # find path center point
    mid_latitude = (max_north + max_south) / 2
    mid_longitude = (max_east + max_west) / 2

    # 'center' api parameter
    center = f"center={mid_latitude},{mid_longitude}"

    # create northeast and southwest point strings
    northeast = f"{max_north},{max_east}"
    southwest = f"{max_south},{max_west}"

    # 'visible' api parameter
    visible = f"markers={northeast}%7C{southwest}"

    # 'maptype' api parameter
    maptype = f"satellite"

    # 'size' api parameter (max = 640x640)
    size = f"size=640x640"

    # 'scale' api parameter (1 = 640x640, 2 = 1280x1280)
    scale = f"scale=1"

    # 'zoom' api parameter (5 = continent, 20 = building) (overridden by 'visible')
    zoom = f"zoom=15"

    # 'format' api parameter (png8, png32, gif, jpg, jpg-baseline)
    format = f"format=png32"

    # 'key' api parameter
    key=f"key={api_key}"

    # full api call url
    url = f"{base_url}?{center}&{visible}&{maptype}&{size}&{scale}&{zoom}&{format}&{key}"

    # add signature to call
    call = sign_url(url, secret)

    # send it
    response = requests.get(call)

    if response.status_code == 200:
        print(response)
        with open('map.png', 'wb') as f:
            f.write(response.content)

    return response.status_code


if __name__ == '__main__':
    status = get_map_image(1.2,2.3,3.4,4.5, "key", "secret")
    print(status)