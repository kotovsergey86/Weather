import requests


def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data.get("current_weather", {})
        return {
            "Температура": f"{weather.get('temperature', 'N/A')}°C",
            "Скорость ветра": f"{weather.get('windspeed', 'N/A')} м/с",
            "Направление ветра": weather.get('winddirection', 'N/A'),
            "Время обновления": weather.get('time', 'N/A')
        }
    else:
        return {"Ошибка": "Не удалось получить данные о погоде"}


moscow_coord = (55.7558, 37.6176)  # Широта и долгота для Москвы

if __name__ == "__main__":
    weather_info = get_weather(*moscow_coord)
    print(weather_info)
