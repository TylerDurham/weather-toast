from glob import glob
import dbus
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["TOMORROW_API_KEY"]
USE_MOCK = True if (os.environ["USE_MOCK"] == "1") else False

def fetch_weather(location='chicago', units='imperial'):
    headers = { "accept": "application/json" }
    if USE_MOCK == True:
        print("Using mock API. Make sure Live Server Visual Studio Code extension [https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer] is running!")
        url = f'http://localhost:5500/sample.json'
    else:
        print("Using real API")
        url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&units={units}&apikey={API_KEY}'
    
    print(f'Calling [${url}]')    
    return requests.get(url, headers=headers)

item = "org.freedesktop.Notifications"

notfy_intf = dbus.Interface(
    dbus.SessionBus().get_object(item, "/"+item.replace(".", "/")), item)

def notify(title, message, icon, timeout=3000):
    print(title)
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
        
    pattern = f'{os.path.join(os.getcwd(), 'images')}/{code}{isNight}_*@2x.png'
    # print(pattern)
    files = glob(pattern)
    return (files[0])
