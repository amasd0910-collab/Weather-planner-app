# 在 Colab 可以執行的簡化版本
import requests

# 獲取天氣資料
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    print(f"城市: {city}")
    print(f"溫度: {data['main']['temp']}°C")
    print(f"天氣: {data['weather'][0]['description']}")

# 測試
api_key = "0012ab17b3143d5072baab8df20cdbdb"
get_weather("Taipei", api_key)
