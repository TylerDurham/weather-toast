from datetime import datetime
from zoneinfo import ZoneInfo
import json
import utils

response = utils.fetch_weather()

weather = json.loads(response.text)["data"]

c_time = datetime.strptime(weather["time"], "%Y-%m-%dT%H:%M:%S%f%z").astimezone(ZoneInfo('America/Chicago'))
# TODO: Figure out if tomorrow.io suppports imperial units or if I need to do the converstions manually.
c_temp = weather["values"]["temperature"]
c_code = weather["values"]["weatherCode"]

# TODO: Need to figure out why some weatherCodes returned from Mockeroo don't have icons associated with them
c_icon = utils.get_icon(c_code, c_time)

message = f'The current temperatur is {c_temp}'

utils.notify("Weather Toast!", message, c_icon)
