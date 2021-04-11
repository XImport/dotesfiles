import psutil
from colorama import Fore
from pynotifier import Notification
import requests
from datetime import date, datetime


class Main:
    def __init__(self):
        Notification(
            title='SYS MONITOR :',
            description=self.sysmon(),
            # On Windows .ico is required, on Linux - .png
            icon_path='path/to/image/file/icon.png',
            duration=5,                              # Duration in seconds
        ).send()

    def sysmon(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        cpu_sensor = []
        for _ in range(1):
            free = str(psutil.virtual_memory().used >> 20)
            total = str(psutil.virtual_memory().total >> 20)
        sensor = psutil.sensors_temperatures().get("coretemp")
        for sen in sensor:

            cpu_sensor.append(sen[1])

        weather = requests.get("http://wttr.in/Tangier?format=%t").text
        date_ = today.strftime("%B %d, %Y")
        return f"📅 {date_}  {current_time} \n🖥️  CPU USAGE : {str(psutil.cpu_percent(interval=1)) } % \n🧠  MEMORY USED : {free}/{total}MB \n 🔥 CPU TEMPETURE IS :{cpu_sensor[1]}%   \n ⛅ CUREENT WEATHER : {weather} ".lstrip()


if __name__ == "__main__":
    Main()
