import streamlit as st
import requests
import datetime
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

date = st.date_input('Date', datetime.date.today())
time = st.time_input('Time', datetime.datetime.now())
date_and_time = str(datetime.datetime.combine(date, time))
pickup_longitude = st.number_input('Pickup Longitude', value=-73.985428)
pickup_latitude = st.number_input('Pickup Latitude', value=40.748817)
dropoff_longitude = st.number_input('Dropoff Longitude', value=-73.977233)
dropoff_latitude = st.number_input('Dropoff Latitude', value=40.752726)
passenger_count = st.number_input('Insert passenger count', 0)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''
params = {
'pickup_datetime': date_and_time,
'pickup_longitude': pickup_longitude,
'pickup_latitude': pickup_latitude,
'dropoff_longitude': dropoff_longitude,
'dropoff_latitude': dropoff_latitude,
'passenger_count': passenger_count
}

'''
3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''


response = requests.get(url, params=params)
if st.button('Get prediction'):
    st.write(round(response.json()['fare'], 2))
st.map(pd.DataFrame({'lat': [pickup_latitude,dropoff_latitude], 'lon': [pickup_longitude,dropoff_longitude]}, columns=['lat', 'lon']))
