from math import cos, asin, sqrt
from firebase import firebase
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import json

FIREBASE_SECRET = "VuvYwZlcU8S2zD8l4arSIp3CdWTo0Xb7BO5FcHSK"
FIREBASE_URL = "https://aquamarine9k1.firebaseio.com/"

def get_iden(table, iden):
	assert iden == 0 or iden == 1
	loc_list = []
	for uid in table:
		 entry = table[uid]
		 if entry["iden"] == iden:
		 	#loc_string = str(entry["loc"].encode("utf-8"))
		 	loc_list.append({"lat": entry["loc"]["lat"], "lng": entry["loc"]["lon"]})

	#print type(loc_list[0])
	return loc_list


def get_location_list():
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	result = fb.get('/users', None)
	loc_list = get_iden(result, 0)
	return loc_list


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def closest(v):
	data = get_location_list()
	print v
	return min(data, key=lambda p: distance(v['lat'],v['lng'],p['lat'],p['lng']))