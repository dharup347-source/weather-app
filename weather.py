"""
Weather App
A simple Python project using OpenWeatherMap API.
"""

import requests

# Replace this with your actual API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    try:
        # Complete API URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

        # Send request to the API
        response = requests.get(url, timeout=10)

        # Convert response to JSON
        data = response.json()

        # Check if city is found
        if data.get("cod") != 200:
            print("City not found. Please check the city name.")
            return

        # Extract useful information
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display weather information
        print("\n" + "=" * 35)
        print(f"Weather in {city.title()}")
        print("=" * 35)
        print(f"Temperature : {temperature}°C")
        print(f"Condition   : {condition.title()}")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_speed} m/s")
        print("=" * 35)

    except requests.exceptions.RequestException:
        print("Error: Unable to connect. Please check your internet connection.")
    except KeyError:
        print("Error: Unexpected response from the server.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("=" * 35)
    print("        WEATHER APP")
    print("=" * 35)

    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()

        if city.lower() == "quit":
            print("Goodbye!")
            break

        if city == "":
            print("Please enter a valid city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
