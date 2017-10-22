from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from utils.get_nearest import *
from utils.getlatlong import *
from utils.get_directions_link import *
from send_sms import *
from utils.getlocname import *
from update_status import *
from utils.exceptions import *


app = Flask(__name__)


@app.route("/sms", methods = ['GET', 'POST'])
def sms_reply():
	message = request.values.get('Body', None)
	phone_num = request.values.get('From', None)

	resp = MessagingResponse()
	
	# user match case
	if "match me at" in message.lower():
		location_phrase = " ".join(message.split(" ")[3:])
		try:
			loc = getlatlong(location_phrase)
			nearest,number = closest(loc)
			link = getdirectionslink([loc["lat"], loc["lng"]], [nearest["lat"], nearest["lng"]])
			resp.message("We found you a match, here is the google maps link: " + link)
			sendmsg(number,"Your help is on the way from "+getlocname([loc["lat"],loc["lng"]]))
			update_receive(0, number, None)
			# create msging channel
			create_connection(number, phone_num)
		except NoMatchException:
			resp.message("Thank you for your good will, but there is no one to help at the moment. Please check back later.")
		except NoPlaceException:
			resp.message("Couldn't recognize location please try with a different location.")

	# match receive case
	elif "receive at" in message.lower():
		location_phrase = " ".join(message.split(" ")[2:])
		try:
			loc = getlatlong(location_phrase)
			update_receive(1, phone_num, loc)
			resp.message("We will inform you once you get a match.")
		except:
			resp.message("Couldn't recognize location please try with a different location.")
	
	elif message.startswith("MSG"):
		msg_phrase = " ".join(message.split(" ")[1:])
		send_anon_msg(phone_num, msg_phrase);

	elif "BYE" == message: 
		remove_connection(phone_num)
		update_receive(0, phone_num, None)
		resp.message("Thank you for using Serve-it!")

	else:
		help_msg = " Hi! If you have chariable donations to a nearby homeless person right now,	you can send \"Match me at <your location>\" to give help. If you are looking for help, send \"Revceive at <your location>\" to open notification alert when someone is ready to help you. If you are all done, send \"BYE\" to end chat and stop notifications and sharing your location."
		resp.message(help_msg)

	return str(resp)

if __name__== "__main__":
	app.run()

