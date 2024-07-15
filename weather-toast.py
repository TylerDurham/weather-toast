from datetime import datetime
from zoneinfo import ZoneInfo
import json
import utils
import argparse

parser = argparse.ArgumentParser(
                    prog='Weather Toast',
                    description='Toasts the current weather.',
                    epilog='More info and source code at https://github.com/TylerDurham/weather-toast')

parser.add_argument('-l', '--location')

args = parser.parse_args()

response = utils.fetch_weather(args.location)

weather = json.loads(response.text)["data"]

c_time = datetime.strptime(weather["time"], "%Y-%m-%dT%H:%M:%S%f%z").astimezone(ZoneInfo('America/Chicago'))
# TODO: Figure out if tomorrow.io suppports imperial units or if I need to do the converstions manually.
c_temp = weather["values"]["temperature"]
c_code = weather["values"]["weatherCode"]
# c_location = weather["location"]["name"]

print (weather)

# TODO: Need to figure out why some weatherCodes returned from Mockeroo don't have icons associated with them
c_icon = utils.get_icon(c_code, c_time)

message = f'The current temperature at is {c_temp}'

utils.notify("Weather Toast!", message, c_icon)
