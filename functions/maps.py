import googlemaps
import os, json

# with open('more_keys.json', 'r') as f:
#     keys = json.load(f)
#     f.close()

# key = keys["google_cse_key"]
key = "AIzaSyD9FYvFyh46hy4gNzBD1lJiM3vfeJqU4tA"

gmaps = googlemaps.Client(key = key)

def streetAndMapsView(locationName):
    query = locationName.replace(" ", "+")
    urlMap = "https://maps.googleapis.com/maps/api/staticmap?center="+query+"&markers="+query+"&size=600x600&key="+key
    urlStreetView = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location="+query+"&key="+key
    return urlMap, urlStreetView

def placeInfo(locationName):
    placeResult  = gmaps.find_place(input=locationName, input_type = "textquery", fields=['name', 'rating','formatted_address', 'geometry', 'place_id'])
    return placeResult

def placeDescription(placeID):
    placeDesc = gmaps.place(placeID)
    return placeDesc

#name = "Cineplex Dundas"
#urlMap, urlStreetView = streetAndMapsView(name)
#placeResult = placeInfo(name)
#print("map view is: "+urlMap)
#print("street view is: "+urlStreetView)
#print(placeResult.items())
