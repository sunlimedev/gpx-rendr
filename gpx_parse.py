# gpx file reader -- returns gps data as python lists

from gpx import read_gpx


def extract_gpx_to_lists(file_path):
    # create lists to store data
    latitudes = []
    longitudes = []
    elevations = []
    times = []

    # choose gpx file
    gpx = read_gpx(file_path)

    # extract data from gpx file
    for trk in gpx.trk:
        for trkseg in trk.trkseg:
            for trkpt in trkseg.trkpt:
                latitudes.append(round(float(trkpt.lat), ndigits=7))
                longitudes.append(round(float(trkpt.lon), ndigits=7))
                elevations.append(round(float(trkpt.ele), ndigits=6))
                times.append(trkpt.time)

    # return lists
    return latitudes, longitudes, elevations, times