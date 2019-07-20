#!/usr/bin/env python
# coding: utf-8

# In[5]:


import herepy
import json
import requests

geocoderApi = herepy.GeocoderApi('rTc2ExgvmtXRk5fJG3IB', 'HwAH1Q70PPoaHB-hqswuHQ')
geocoderReverseApi = herepy.GeocoderReverseApi('rTc2ExgvmtXRk5fJG3IB', 'HwAH1Q70PPoaHB-hqswuHQ')

from locations import location_data

loc = location_data()


# In[6]:



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

