import pygal

class WeatherDisplay:

    def __init__(self, filename="weather.txt"):
        self.filename = filename

    def generate_graph(self):

        times = []
        temperatures = []

        with open(self.filename, "r") as file:
            for line in file:
                data = line.strip().split(",")

                times.append(data[0][-8:])
                temperatures.append(float(data[1]))

        chart = pygal.Line()

        chart.title = "Temperature Logger"

        chart.x_labels = times

        chart.add("Temperature", temperatures)

        chart.render_to_file("temperature.svg")

        print("Graph Generated.")