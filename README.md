# 🌤 Weather App

Welcome to the Enhanced Weather App! This application allows you to fetch and display current weather information for any city around the world using the OpenWeatherMap API.

## Features

- 🌍 **Global Weather Data**: Retrieve weather information for any city worldwide.
- 🌡️ **Temperature Details**: Get the current temperature and "feels like" temperature.
- 🌤️ **Weather Description**: Understand the current weather conditions with a detailed description.
- 💧 **Humidity Levels**: Check the humidity percentage.
- 🌬️ **Wind Speed**: Know the current wind speed in km/h.
- 🌀 **Pressure**: Get the atmospheric pressure in hPa.
- 🌅 **Sunrise and Sunset Times**: See the sunrise and sunset times in UTC.

## Getting Started

These instructions will help you set up and run the Enhanced Weather App on your local machine.

### Prerequisites

- Python 3.x
- `requests` library

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Goyam02/WEATHER-APP.git
   cd WEATHER-APP

2. **Install the required dependencies:**

    ```bash
    pip install requests

3. **Get your API key:**

    - Sign up for a free API key at OpenWeatherMap.<br>
    - Replace the api_key variable in the fetch_weather function with your valid API key.

### Usage

1. **Run the application:**
    ```bash
    python weather.py

2. **Enter the city name when prompted:**
    ```bash
    🌤 Welcome to the Enhanced Weather App!
    Enter city name: London

3. **View Weather Deatils:**
    ```bash
- 🌍 Weather Details for London, GB:
-  🌡️ Temperature: 15°C
- 🥶 Feels Like: 13°C
- 🌤️ Weather: Clear sky
- 💧 Humidity: 60%
- 🌬️ Wind Speed: 5 km/h
- 🌀 Pressure: 1012 hPa
- 🌅 Sunrise: 07:30:00 UTC
- 🌇 Sunset: 16:45:00 UTC

## Contributing

Feel free to contribute to this project by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Goyam02/Weather-App/blob/main/LICENSE) file for details.

## Acknowledgements

- Thanks to [OpenWeatherMap](https://openweathermap.org/api) for providing the weather data API.