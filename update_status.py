from firebase import firebase
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from utils.get_nearest import *

FIREBASE_SECRET = "VuvYwZlcU8S2zD8l4arSIp3CdWTo0Xb7BO5FcHSK"
FIREBASE_URL = "https://aquamarine9k1.firebaseio.com/"

def update_receive(receive_flag, phone_num, lnglat):
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	result = fb.get('/users', None)
	node_uid = get_node(result, phone_num)

	if node_uid == None:
		user = {"loc": lnglat, "notif": 1, "phone_num": phone_num}
		fb.post("/users", user)
	else:
		result[node_uid]["notif"] = receive_flag
		if lnglat != None:
			result[node_uid]["loc"] = lnglat
		fb.post("/users", result[node_uid])
		fb.delete('/users/'+node_uid, None)


def get_node(table, phone_num):
	for uid in table:
		 entry = table[uid]
		 if entry["phone_num"] == phone_num:
		 	return uid
	return None