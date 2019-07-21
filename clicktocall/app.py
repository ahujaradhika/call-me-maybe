from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for

from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import herepy
import json
import requests

def get_phone_number():
    loc = worker()
    geocoderApi = herepy.GeocoderApi('rTc2ExgvmtXRk5fJG3IB', 'HwAH1Q70PPoaHB-hqswuHQ')
    geocoderReverseApi = herepy.GeocoderReverseApi('rTc2ExgvmtXRk5fJG3IB', 'HwAH1Q70PPoaHB-hqswuHQ')
    response = requests.get('https://places.cit.api.here.com/places/v1/autosuggest?at=37.787541999999995,-122.4109585&q=police&station&app_id=rTc2ExgvmtXRk5fJG3IB&app_code=HwAH1Q70PPoaHB-hqswuHQ')

    parsed = json.loads(response.text)

    url = parsed['results'][0]['href']
    response2 = requests.get(url)
    parsed2 = json.loads(response2.text)
    station_url = parsed2['results']['items'][0]['href']

    response3 = requests.get(station_url)
    parsed3 = json.loads(response3.text)
    phoneNumber = parsed3['contacts']['phone'][0]['value']
    print(phoneNumber)
    # phoneNumber = '747-334-9366'
    # print(phoneNumber)

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')


# Route for Click to Call demo page.
@app.route('/')
def index():
    return render_template('index.html',
                           configuration_error=None)


# Voice Request URL
@app.route('/call', methods=['POST'])
def call():
    # Get phone number we need to call
    phone_number = request.form.get('phoneNumber', None)

    try:
        twilio_client = Client(app.config['TWILIO_ACCOUNT_SID'],
                               app.config['TWILIO_AUTH_TOKEN'])
    except Exception as e:
        msg = 'Missing configuration variable: {0}'.format(e)
        return jsonify({'error': msg})

    try:
        twilio_client.calls.create(from_=app.config['TWILIO_CALLER_ID'],
                                   to=phone_number,
                                   url=url_for('.outbound',
                                               _external=True))
    except Exception as e:
        app.logger.error(e)
        return jsonify({'error': str(e)})

    return jsonify({'message': 'Call incoming!'})


@app.route('/outbound', methods=['POST'])
def outbound():
    response = VoiceResponse()

    response.say("Thank you for calling, we will redirect you to your selected personal.",
                 voice='alice')
    response.dial(phoneNumber)
    '''
    # Uncomment this code and replace the number with the number you want
    # your customers to call.
    response.number("+16518675309")
    '''
    return str(response)

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


# Route for Landing Page after Heroku deploy.
@app.route('/landing.html')
def landing():
    return render_template('landing.html',
                           configuration_error=None)
