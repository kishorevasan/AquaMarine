from twilio.rest import Client
from firebase import firebase
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

ACCOUNT_SID = "AC443f82c9a189a3d1e34c6ad1e4b1acb3"
AUTH_TOKEN = "37dbb6ca2c20abac6485e3c080b5795a"

FIREBASE_SECRET = "VuvYwZlcU8S2zD8l4arSIp3CdWTo0Xb7BO5FcHSK"
FIREBASE_URL = "https://aquamarine9k1.firebaseio.com/"


def sendmsg(number,body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(to=number,from_="+15107562698",body=body)
    
def create_connection(homeless_num, user_num):
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	connection = {"homeless": homeless_num, "user": user_num}
	fb.post("/connections", connection)
	create_msg = "Your connection with your match has been established. Type MSG <your message> to chat with your match. Type BYE to end the connection."
	sendmsg(homeless_num, create_msg)
	sendmsg(user_num, create_msg)

def remove_connection(phone_num):
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	table = fb.get('/connections', None)
	if table != None:
		for cid in table:
			if table[cid]["homeless"] == phone_num or table[cid]["user"] == phone_num:
				remove_msg = "Your connection has been removed."
				sendmsg(table[cid]["homeless"], remove_msg)
				sendmsg(table[cid]["user"], remove_msg)
				fb.delete("/connections/"+cid, None)

def send_anon_msg(from_, body):
	fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=None)
	table = fb.get('/connections', None)
	to = None

	if table != None:
		for cid in table:
			if table[cid]["homeless"] == from_:
				to = table[cid]["user"]
			elif table[cid]["user"] == from_:
				to = table[cid]["homeless"]
		if to == None:
			assert False
		else:
			sendmsg(to, body)
