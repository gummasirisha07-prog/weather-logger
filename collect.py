from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

class WeatherCollector:

    def __init__(self, filename="weather.txt"):
        self.filename = filename

    def read_sensor_data(self):
        temperature = round(sense.get_temperature(), 2)
        humidity = round(sense.get_humidity(), 2)
        pressure = round(sense.get_pressure(), 2)

        return temperature, humidity, pressure

    def save_data(self):
        temp, hum, pres = self.read_sensor_data()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.filename, "a") as file:
            file.write(f"{timestamp},{temp},{hum},{pres}\n")

        print("Weather data saved.")