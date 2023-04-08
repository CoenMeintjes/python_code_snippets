# =========================================== #
# py4e Week_6 (Web_Data) Parse JSON
# =========================================== #
# Exercise 1
# =========================================== #

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
uh = urllib.request.urlopen(url)

print('Retrieving: ', url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
# print the js data with .dumps (pretty print) so that we can see the object lists+dict 
# print(json.dumps(js, indent=4))

lst = list()
# for loop to iterate through the objects in the "comments" key of the master object
for items in js["comments"]:
    # print(items["count"])
    lst.append(items["count"])

print('Count: ', len(lst))    
print('Total comments:',sum(lst))

# =========================================== #
# Exercise 2
# =========================================== #

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    id = js['results'][0]['place_id']
    print('Placi id:',id)
    # location = js['results'][0]['formatted_address']
    # print(location)