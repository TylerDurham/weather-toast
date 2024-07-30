from glob import glob
import dbus
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["TOMORROW_API_KEY"]
USE_MOCK = True if (os.environ["USE_MOCK"] == "1") else False
MOCK_API_KEY = os.environ["MOCKAROO_API_KEY"]

def fetch_weather():
    headers = { "accept": "application/json" }
    if USE_MOCK == True:
        print("Using mock API")
        headers = {
            "accept": "application/json",
            "X-API-Key": MOCK_API_KEY
        }
        url = f'https://my.api.mockaroo.com/tomorrow.io.json'
    else:
        print("Using real API")
        url = f'https://api.tomorrow.io/v4/weather/realtime?location=chicago&apikey={API_KEY}'
        
    return requests.get(url, headers=headers)

item = "org.freedesktop.Notifications"

notfy_intf = dbus.Interface(
    dbus.SessionBus().get_object(item, "/"+item.replace(".", "/")), item)

def notify(title, message, icon, timeout=3000):

    notfy_intf.Notify(
        "", 
        0, 
        icon, 
        title, 
        message,
        [], 
        {"urgency": 1}, 
        timeout
    )
    
def get_icon(code, time):

    isNight = 0 if (time.hour % 12 == 0) else 1
    print(isNight)        
    pattern = f'{os.path.join(os.getcwd(), "images")}/{code}{isNight}_*@2x.png'
    print(pattern)
    files = glob(pattern)
    return (files[0])
