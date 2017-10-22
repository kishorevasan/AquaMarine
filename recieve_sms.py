from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from utils.get_nearest import *
from utils.getlatlong import *
from utils.get_directions_link import *


app = Flask(__name__)


@app.route("/sms", methods = ['GET', 'POST'])
def sms_reply():
	message = request.values.get('Body', None)
	resp = MessagingResponse()
	resp.message("Sorry, I don't quite understand what you mean...")

	# user match case
	if "match me at" in message.lower():
		location_phrase = " ".join(message.split(" ")[3:])
		loc = getlatlong(location_phrase)
		nearest = closest(loc)

		link = getdirectionslink([loc["lat"], loc["lng"]], [nearest["lat"], nearest["lng"]])
		resp.message("We found you a match, here is the google maps link: " + link)

	# match receive case
	elif "receive at" in message.lower():
		location_phrase = " ".join(message.split(" ")[2:])
		loc = getlatlong(location_phrase)

		#


	return str(resp)

if __name__== "__main__":
	app.run()

