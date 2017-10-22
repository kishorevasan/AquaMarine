from twilio.rest import Client

ACCOUNT_SID = "AC443f82c9a189a3d1e34c6ad1e4b1acb3"
AUTH_TOKEN = "37dbb6ca2c20abac6485e3c080b5795a"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(to="+16506913638",from_="+15107562698",body="Sup")
