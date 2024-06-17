import time
from plyer import notification
import requests

while True:
    api_url = 'https://api.api-ninjas.com/v1/jokes?random'
    response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
    if response.status_code == requests.codes.ok:
        joke=response.json()[0]["joke"]
    notification.notify(title='Joke', message=joke, app_icon='funny.ico', timeout=7)
    time.sleep(20)