import requests
from src.utils.api_keys import WEATHER_API_KEY

def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"O clima em {city} é {weather} com temperatura de {temperature}°C."
    return "Não foi possível encontrar a previsão do tempo para a cidade informada."
