#!flask/bin/python
import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
import herepy
import requests

# Flask App
app = Flask(__name__)

# Here API credentials
geocoderApi = herepy.GeocoderApi('rTc2ExgvmtXRk5fJG3IB', 'HwAH1Q70PPoaHB-hqswuHQ')
geocoderReverseApi = herepy.GeocoderReverseApi('rTc2ExgvmtXRk5fJG3IB', 'HwAH1Q70PPoaHB-hqswuHQ')

@app.route("/")
def get_phone_number():
    loc = worker()
    response = requests.get('https://places.cit.api.here.com/places/v1/autosuggest?at='+loc+'&q=police&station&app_id=rTc2ExgvmtXRk5fJG3IB&app_code=HwAH1Q70PPoaHB-hqswuHQ')

    parsed = json.loads(response.text)

    url = parsed['results'][0]['href']
    response2 = requests.get(url)
    parsed2 = json.loads(response2.text)
    station_url = parsed2['results']['items'][0]['href']

    response3 = requests.get(station_url)
    parsed3 = json.loads(response3.text)
    phone_number = parsed3['contacts']['phone'][0]['value']
    print(phone_number)

# main page route
@app.route("/")
def output():
	return render_template("index.html", name="Joe")

# receiver
@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
    data = request.form.get('location_data')
    print(data)
    
    latitude = request.values['location_data[latitude]']
    longitude = request.values['location_data[longitude]']

    print(type(latitude))
    print(type(longitude))

    location_info = latitude + ',' + longitude
    print(location_info)

    return location_info

# run the development server
if __name__ == "__main__":
    app.run("0.0.0.0", "5000")

#!flask/bin/python

# import sys

# from flask import Flask, render_template, request, redirect, Response
# import random, json

# app = Flask(__name__)

# @app.route('/')
# def output():
# 	# serve index template
# 	return render_template('index.html', name='Joe')

# @app.route('/receiver', methods = ['POST'])
# def worker():
# 	# read json + reply
# 	data = request.get_json()
# 	result = ''

# 	for item in data:
# 		# loop over every row
# 		result += str(item['make']) + '\n'

# 	return result

# if __name__ == '__main__':
# 	# run!
# 	app.run()