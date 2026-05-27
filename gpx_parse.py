from gpx import read_gpx

latitudes = []
longitudes = []
elevations = []
times = []

gpx = read_gpx("test_ride.gpx")

for trk in gpx.trk:
    for trkseg in trk.trkseg:
        for trkpt in trkseg.trkpt:
            latitudes.append(trkpt.lat)
            longitudes.append(trkpt.lon)
            elevations.append(trkpt.ele)
            times.append(trkpt.time)

print(max(latitudes))
print(min(latitudes))

print(max(longitudes))
print(min(longitudes))

center = ((max(latitudes)+min(latitudes))/2, (max(longitudes)+min(longitudes))/2)

print(center)