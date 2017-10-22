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
		 loc_list.append(entry["loc"])
	return loc_list


def get_location_list():
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	result = fb.get('/users', None)
	loc_list = get_iden(result, 0)
	return loc_list


def write_to_fire(content):
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	data = {'url': content, 'address': "address", 'name': "name"}
	#sent = json.dumps(data)
	result = fb.post("/something", data)

def delete_in_fire():
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	fb.delete('/something/-Kx3inCvSEAUIlRpoAOd', None)


