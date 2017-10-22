from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from utils.get_nearest import *
from utils.getlatlong import *
from utils.get_directions_link import *
from send_sms import *
from utils.getlocname import *
from update_status import *


app = Flask(__name__)


@app.route("/sms", methods = ['GET', 'POST'])
def sms_reply():
	message = request.values.get('Body', None)
	phone_num = request.values.get('From', None)

	resp = MessagingResponse()


	# user match case
	if "match me at" in message.lower():
		location_phrase = " ".join(message.split(" ")[3:])
		loc = getlatlong(location_phrase)
		nearest,number = closest(loc)

		link = getdirectionslink([loc["lat"], loc["lng"]], [nearest["lat"], nearest["lng"]])
		resp.message("We found you a match, here is the google maps link: " + link)
		sendmsg(number,"Your help is on the way from "+getlocname([loc["lat"],loc["lng"]]))

	# match receive case
	elif "receive at" in message.lower():
		location_phrase = " ".join(message.split(" ")[2:])
		loc = getlatlong(location_phrase)
		update_receive(1, phone_num, loc)
		resp.message("We will inform you once you get a match.")

	elif "BYE" == message: 
		update_receive(0, phone_num, None)
		resp.message("Thank you for using Serve-it!")

	else:
		resp.message("Type match me at <Location> to give help or receive at <Location> to get help")

	return str(resp)

if __name__== "__main__":
	app.run()

