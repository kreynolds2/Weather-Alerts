import requests

response = requests.get("https://api.weather.gov/")
print(response.status_code)