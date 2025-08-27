"""
Weather App (CLI using OpenWeatherMap API)
Requires: pip install requests
Usage: python weather_app.py CITY_NAME YOUR_API_KEY
"""
import sys, requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def kelvin_to_c(k): return k - 273.15

def get_weather(city, api_key):
    r = requests.get(API_URL, params={"q": city, "appid": api_key})
    r.raise_for_status()
    data = r.json()
    main = data["main"]
    desc = data["weather"][0]["description"]
    temp_c = kelvin_to_c(main["temp"])
    feels_c = kelvin_to_c(main["feels_like"])
    return {
        "city": data["name"],
        "temp_c": round(temp_c, 1),
        "feels_c": round(feels_c, 1),
        "desc": desc
    }

def main():
    if len(sys.argv) < 3:
        print("Usage: python weather_app.py CITY_NAME YOUR_API_KEY")
        sys.exit(1)
    city, key = sys.argv[1], sys.argv[2]
    try:
        info = get_weather(city, key)
        print(f"{info['city']}: {info['temp_c']}°C (feels {info['feels_c']}°C), {info['desc']}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
