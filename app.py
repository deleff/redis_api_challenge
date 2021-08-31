import time, redis, flask
from flask import Flask, request, jsonify, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return '<h1>Python api call with redis</h1> </br>curl /set?id=value&data=value to set a value </br></br> curl /get?id=value to get the value'

@app.route('/healthcheck')
def healthcheck():
    return '{"status":"ok"}'

@app.route('/set')
def set():
  # Sets the value of a key given url parameters 'key' and 'value'.
  key = request.args.get('id')
  value = request.args.get('data')
  cache.set(key, value.encode('utf-8'))
  return '<h1>Added id: {}, data: {}</h1>'.format(key,value)

@app.route('/get')
def get():
  # returns the value of a key in a cache.
  key = request.args.get('id')
  value = cache.get(key).decode('utf-8')
  return '<h1>{}</h1>'.format(value)