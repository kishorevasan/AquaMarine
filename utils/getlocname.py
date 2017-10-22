from geopy.geocoders import Nominatim

def getlocname(location):
    geolocator = Nominatim()
    return geolocator.reverse(str(location[0])+","+str(location[1])).address
