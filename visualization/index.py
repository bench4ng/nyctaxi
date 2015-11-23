import time
import json
import datetime
import sys
from bottle import route, run, template, request, static_file

@route('/')
def index():
    return 'BDS Project'

@route('/ClusterPoint')
def map():
    return static_file('visualization.html', root='./')

@route('/MaxTip')
def map():
    return static_file('Route.html', root='./')
    
run(host='0.0.0.0',port=3050, reloader=True, debug=True, server = 'paste')
