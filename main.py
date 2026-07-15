from collect import WeatherCollector
from display import WeatherDisplay
import time

collector = WeatherCollector()

print("Collecting Weather Data...")

for i in range(10):
    collector.save_data()
    time.sleep(2)

display = WeatherDisplay()

display.generate_graph()

print("Done.")