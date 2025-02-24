import numpy as np


class Sensor:
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location

    def generate_measurement(self):
        """
        Generiert eine neue Messung mit normalverteilten Werten und zufälligen Ausreißern.
        """
        # Normalverteilte Sensordaten
        temperature = np.random.normal(loc=22.0, scale=1.5)  # °C
        humidity = np.random.normal(loc=60.0, scale=10.0)  # %
        pressure = np.random.normal(loc=1013.0, scale=5.0)  # hPa
        wind_speed = np.random.normal(loc=5.0, scale=2.0)  # m/s
        wind_direction = np.random.normal(loc=180.0, scale=30.0)  # Grad

        # Ausreißer zufällig einfügen (10% Wahrscheinlichkeit pro Messwert)
        if np.random.rand() < 0.1:
            # Unplausibel hohe Temperatur
            temperature = np.random.normal(loc=40.0, scale=5.0)
        if np.random.rand() < 0.1:
            # Extrem hohe Luftfeuchtigkeit
            humidity = np.random.normal(loc=100.0, scale=15.0)
        if np.random.rand() < 0.1:
            # Unrealistischer Luftdruck
            pressure = np.random.normal(loc=900.0, scale=20.0)

        # Sensor-ID oder Location mit Fehlern versehen (5% Wahrscheinlichkeit)
        sensor_id = self.sensor_id if np.random.rand() > 0.05 else None
        location = self.location if np.random.rand() > 0.05 else "UNKNOWN"

        # Measuremnt-Objekt zurückgeben
        return {
            "sensor_id": sensor_id,
            "location": location,
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "wind_speed": wind_speed,
            "wind_direction": wind_direction,
        }
