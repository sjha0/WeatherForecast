import streamlit as st
import requests

# API key and base URL
API_KEY = "ce2a5f295cbe476a9f4102909251204"  # <-- Replace this with your new key
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# Streamlit page configuration
st.title("Weather Forecast")
st.write("Enter the city name to get the weather forecast.")

# User input for city
city = st.text_input("City", "Panchkula")

# Fetch weather data
if city:
    url = f"{BASE_URL}?key={API_KEY}&q={city},India"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        location = data['location']
        current_weather = data['current']

        # Display the results
        st.subheader(f"Weather in {location['name']}, {location['region']}, {location['country']}")
        st.write(f"Temperature: {current_weather['temp_c']}°C")
        st.write(f"Condition: {current_weather['condition']['text']}")
        st.write(f"Humidity: {current_weather['humidity']}%")
        st.write(f"Wind Speed: {current_weather['wind_kph']} kph")
        st.image(f"https:{current_weather['condition']['icon']}", width=100)
    else:
        st.error("Could not fetch weather data. Please try again.")



