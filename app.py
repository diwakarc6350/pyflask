#!/usr/bin/env python
# encoding: utf-8

import json
import urllib3
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    banner="""
    <html>
    Welcome to the weather app api. <br>
    You can get the weather information by calling  <br>
    http://{WEATHER_APP_URL}/weather?city=dallas <br>
    </html>
    """    
    return banner

@app.route('/health')
def health():
    healthcheck="""
    {"status":"OK"}
    """    
    return healthcheck

@app.route('/weather', methods=['GET'])
def weather_info():  
    try:
        args = request.args
        key = 'city' 
        print(args.keys())   
        if key in args.keys():
            return get_data_from_goweather(args[key])
        else:
            error_message="city argument in request is missing"
            response = app.response_class(
                            response=error_message,
                            status=400,
                            mimetype='application/text'
                        )
            return response
    except:
        error_message = "An unexpected error occured"
        response = app.response_class(
                        response=error_message,
                        status=500,
                        mimetype='application/text'
                    )
        return response
    

def get_data_from_goweather(city):    
    try:
        url = "https://goweather.herokuapp.com/weather/" + city        
        http = urllib3.PoolManager()  
        resp = http.request('GET', url)
        print(resp.status)
        if (resp.status==200):
            response = json.loads(resp.data.decode('utf-8'))
            return response
        else:            
            error_message = "Unable to fetch data from goweather.herokuapp.com"
            response = app.response_class(
                            response=error_message,
                            status=500,
                            mimetype='application/text'
                        )
            return response
    except:
        error_message="""
        An unexpected error occured, unable to get weather 
        information from goweather.herokuapp.com
        """
        response = app.response_class(
                            response=error_message,
                            status=500,
                            mimetype='application/text'
                        )
        return response

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


    