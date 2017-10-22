from geopy.geocoders import Nominatim

def getlocname(location):
    geolocator = Nominatim()
    return str(geolocator.reverse(str(location[0])+","+str(location[1])))
