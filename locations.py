#!flask/bin/python
import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
app = Flask(__name__)

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

    return render_template("index.html", latitude=latitude, longitude=longitude)

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