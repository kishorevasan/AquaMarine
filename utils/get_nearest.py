from math import cos, asin, sqrt
from firebase import firebase
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import json

FIREBASE_SECRET = "VuvYwZlcU8S2zD8l4arSIp3CdWTo0Xb7BO5FcHSK"
FIREBASE_URL = "https://aquamarine9k1.firebaseio.com/"



def get_location_list():
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	table = fb.get('/users', None)
	loc_list = []
	ids = []
	for uid in table:
		if table[uid]["notif"] == 1:
			entry = table[uid]
			loc_list.append({"lat": entry["loc"]["lat"], "lng": entry["loc"]["lng"]})
			ids.append(entry["phone_num"])

	return [loc_list,ids]


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def closest(v):
	data,ids = get_location_list()
	minloc = min(data, key=lambda p: distance(v['lat'],v['lng'],p['lat'],p['lng']))
	number = next(index for (index, d) in enumerate(data) if d["lat"] == minloc["lat"] and d["lng"]== minloc["lng"])
	return [minloc,ids[number]]
