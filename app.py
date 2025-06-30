import streamlit as st
import requests

st.title(" Visual Crossing Weather App")
st.write("Get real-time weather updates for any city in the world.")

city = st.text_input("Enter city name", "Karachi")


api_key = "B3D6NSSNKMSZ3F8DCG6E85JR3"  

url = (
    f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    f"{city}?unitGroup=metric&key={api_key}&contentType=json"
)

if city:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        today = data["days"][0]

        st.success(f"Weather in {data['resolvedAddress']} ({data['timezone']})")
        st.write(f" Date: {today['datetime']}")
        st.write(f" Condition: {today['conditions']}")
        st.write(f" Temperature: {today['temp']} °C")
        st.write(f" Feels Like: {today['feelslike']} °C")
        st.write(f" Humidity: {today['humidity']}%")
        st.write(f" Wind Speed: {today['windspeed']} km/h")
        st.write(f" Sunrise: {today['sunrise']}")
        st.write(f" Sunset: {today['sunset']}")
    else:
        st.error("City not found or API error. Check city name or key.")
