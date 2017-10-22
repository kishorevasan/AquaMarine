from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from utils.get_nearest import *
from utils.getlatlong import *

app = Flask(__name__)

@app.route("/sms", methods = ['GET', 'POST'])
def sms_reply():
	message = request.values.get('Body', None)

	loc = getlatlong(message)

	resp = MessagingResponse()
	resp.message("Closet: {}".format(loc))

	return str(resp)

if __name__== "__main__":
	app.run()