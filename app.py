from flask import Flask,jsonify, Response, request
import math
import hashlib
import json
import requests
from redis import Redis, RedisError
import redis
from collections import defaultdict

#--------------instantiate the Flask object--------------#
app = Flask(__name__)


#URL used for Slack bot
SLACK_URL = 'https://hooks.slack.com/services/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'

#--------------App Routes--------------#
@app.route("/")
def index():
	return "Welcome to the Project API"

#--------------Project 6 Continuation Redis--------------#
#Adding the Redis port
red = redis.Redis(host='redis', port=6379, db=0)


#--------------CLI--------------#
@app.route('/CLI/<int:n>')
from argparse import ArgumentParser
import csv
import json
from pprint import pprint
import requests


def read():
   product_list_url = 'http://localhost:5000/'
   response = requests.get(product_list_url)

   return response.json()

def save(data):
    with open('product_data.csv', 'w') as f:
        field_names = ['id', 'name', 'product_id', 'description']
    writer = csv.DictWriter(f, fieldnames=field_names)

    writer.writeheader()
    for row in data.json():
        writer.writerow(row)


if __name__ == '__main__':
   parser = ArgumentParser(description='A command line tool for interacting with our API')
   parser.add_argument('-r', '--read', action='store_true', help='Sends a GET request to the product API.')
   parser.add_argument('-p', '--preview', action='store_true', help='Shows us a preview of the data.')
   parser.add_argument('-s', '--save', action='store_true', help='Save the response.')
   args = parser.parse_args()

   if args.read:
       read()
   if args.preview:
       preview(read())
   else:
       print('Use the -h or --help flags for help')


	
#--------------md5 hash converter--------------#
@app.route('/md5/<string:input>', methods=['GET'])
def get_md5(input):
	res = hashlib.md5(input.encode())
	return jsonify(input=input,output=str(res.hexdigest()))

#--------------factorial converter--------------#
@app.route('/factorial/<int:n>')
def factorial(n):
    res1 = math.factorial(n)
    return jsonify(input=n, output=res1)


#--------------fibonacci endpoint--------------#
@app.route('/fibonacci/<int:n>', methods=['GET'])
def fib(n):
    a, b = 0, 1
    array = [0]
    while b <= n:
        array.append(b)
        a, b = b, a+b

    if n<=0:
        print("Incorrect input, please put a positive number")
    
    else:

        return jsonify(input=n, output=array)

#--------------prime endpoint--------------#
@app.route('/is-prime/<int:n>')
def prime_check(n):
    number = isinstance(n, int)
    if number == True:
        if n > 1: 
            for i in range(2, n):
                if (n % i) == 0:
                    return jsonify(input=n, output=False)
            return jsonify(input=n, output=True)
        elif(n == 0):
            return jsonify(input=n, output=False)            
        elif(n == 1):
            return jsonify(input=n, output=False)             
    else: 
        return jsonify(input=n, output=True)


@app.route('/keyval/<string>')
#--------------slack alert endpoint--------------#
@app.route('/slack-alert/<string:x>')
def slack_post(x):
    data = { 'text' : x }
    resp = requests.post(SLACK_URL, json=data)
    if resp.status_code == 200:
        result = True
        verification = "Your message was sent succesfully."
    else:
        result = False
        verification = "Unable to post your message."
    return jsonify(
    input=x,
    message=verification,
    output=result
    ), 200 if resp.status_code==200 else 400

    
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
