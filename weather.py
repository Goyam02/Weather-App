import requests
from datetime import datetime, timezone

def fetch_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your valid API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"], tz=timezone.utc).strftime('%H:%M:%S UTC')
        sunset = datetime.fromtimestamp(data["sys"]["sunset"], tz=timezone.utc).strftime('%H:%M:%S UTC')

        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "sunrise": sunrise,
            "sunset": sunset,
            "description": data["weather"][0]["description"],
        }
        return weather
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except KeyError:
        print("City not found. Please enter a valid city name.")
        return None

def main():
    print("🌤 Welcome to the Enhanced Weather App!")
    city = input("Enter city name: ")
    weather = fetch_weather(city)

    if weather:
        print(f"\n🌍 Weather Details for {weather['city']}, {weather['country']}:")
        print(f"- 🌡️ Temperature: {weather['temperature']}°C")
        print(f"- 🥶 Feels Like: {weather['feels_like']}°C")
        print(f"- 🌤️ Weather: {weather['description'].capitalize()}")
        print(f"- 💧 Humidity: {weather['humidity']}%")
        print(f"- 🌬️ Wind Speed: {weather['wind_speed']} km/h")
        print(f"- 🌀 Pressure: {weather['pressure']} hPa")
        print(f"- 🌅 Sunrise: {weather['sunrise']}")
        print(f"- 🌇 Sunset: {weather['sunset']}")
    else:
        print("Unable to fetch weather details.")

if __name__ == "__main__":
    main()
