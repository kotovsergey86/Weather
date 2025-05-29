import requests

CITY_COORDINATES = {
    "Москва": (55.7558, 37.6176),
    "Санкт-Петербург": (59.9343, 30.3351),
    "Новосибирск": (55.0084, 82.9357)
}

def fetch_weather_data(latitude, longitude):
    """
    Выполняет запрос к API погоды с указанными координатами.

    :param latitude: Широта города
    :param longitude: Долгота города
    :return: Ответ от API в формате Response
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )
    return requests.get(url)

def parse_weather_data(response):
    """
    Обрабатывает ответ от API и извлекает данные о текущей погоде.

    :param response: Ответ от API в формате Response
    :return: Словарь с информацией о погоде или ошибкой
    """
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

def get_city_coordinates(city_name, city_coordinates=None):
    """
    Возвращает координаты города по его названию.

    :param city_name: Название города
    :param city_coordinates: Пользовательский словарь с координатами (опционально)
    :return: Кортеж с координатами или None
    """
    if city_coordinates is None:
        city_coordinates = CITY_COORDINATES
    return city_coordinates.get(city_name)

def get_weather_by_city(city_name):
    """
    Получает данные о текущей погоде в указанном городе.

    :param city_name: Название города
    :return: Словарь с информацией о погоде или ошибкой
    """
    coordinates = get_city_coordinates(city_name)
    if not coordinates:
        return {"Ошибка": f"Город '{city_name}' не найден в базе данных координат."}

    response = fetch_weather_data(*coordinates)
    return parse_weather_data(response)

if __name__ == "__main__":
    city = "Москва"
    weather_info = get_weather_by_city(city)
    print(weather_info)
