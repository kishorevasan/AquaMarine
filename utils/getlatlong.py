import requests

def getlatlong(location):
	location = '+'.join("Mary Gates Hall")

	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+location)
	resp_json_payload = response.json()

	return resp_json_payload['results'][0]['geometry']['location']