import os
import tempfile

import pytest
import json

from app import app

@pytest.fixture
def client():
    app.config.update({'TESTING': True})

    with app.test_client() as client:
        yield client

def test_index_page_banner(client):
    resp = client.get('/')
    assert b'Welcome to the weather app api' in resp.data
    assert b'You can get the weather information' in resp.data

def test_index_has_200_status_code(client):
    resp = client.get('/')        
    assert resp.status_code is 200

def test_weather_api_has_200_status_code(client):
    resp = client.get('/weather?city=boston')        
    assert resp.status_code is 200

def test_weather_api_raises_city_missing_error(client):
    resp = client.get('/weather?citysss=paris')        
    assert b'city argument in request is missing' in resp.data    

def test_weather_api_shows_weather_information(client):
    resp = client.get('/weather?city=boston')            
    assert resp.status_code is 200    
   
    data = json.loads(resp.data)     
    assert data["description"] is not None
    assert data["forecast"] is not None
    assert data["wind"] is not None
    assert data["temperature"] is not None
    