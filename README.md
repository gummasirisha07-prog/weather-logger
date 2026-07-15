# Weather Logger

A Python-based Weather Logger application that collects environmental data from the Raspberry Pi Sense HAT sensors, stores the readings in a text file, and generates a graphical visualization.

---

## Features

- Read Temperature
- Read Humidity
- Read Pressure
- Store weather data in a text file
- Generate a temperature graph using Pygal
- Modular Python code
- Docker support

---

## Technologies Used

- Python 3.11
- Sense HAT
- Pygal
- Docker

---

## Folder Structure

```
weather-logger/
│
├── main.py
├── collect.py
├── display.py
├── weather.txt
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── LICENSE
├── .gitignore
└── images/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/weather-logger.git
cd weather-logger
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## Sample Output

```
2026-07-15 10:30:15,28.4,62.1,1008.3
2026-07-15 10:30:17,28.5,61.9,1008.4
```

---

## Graph Output

The application generates

```
temperature.svg
```

showing temperature changes over time.

---

## Future Improvements

- CSV Export
- SQLite Database
- Live Dashboard
- MQTT Support
- Cloud Storage

---

## Author

Sirisha G

Electronics and Communication Engineering

---

## License

MIT License   