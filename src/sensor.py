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
        temperature = np.random.normal(loc=11.19, scale=1.5)  # °C
        humidity = np.random.normal(loc=77.0, scale=10.0)  # %
        wind_speed = np.random.normal(loc=4.3, scale=2.0)  # km/h

        # Ausreißer zufällig einfügen (1% Wahrscheinlichkeit pro Messwert)
        if np.random.rand() < 0.001:
            temperature = np.random.normal(
                loc=80.0, scale=5.0
            )  # Unplausibel hohe Temperatur
        if np.random.rand() < 0.001:
            humidity = np.random.normal(
                loc=150.0, scale=15.0
            )  # Zu hohe Luftfeuchtigkeit
        if np.random.rand() < 0.001:
            wind_speed = np.random.normal(
                loc=500.0, scale=20.0
            )  # Unrealistische Windgeschwindigkeit

        # Sensor-ID oder Location mit Fehlern versehen (1% Wahrscheinlichkeit)
        sensor_id = self.sensor_id if np.random.rand() > 0.001 else "NULL"
        location = self.location if np.random.rand() > 0.001 else "UNKNOWN"

        # Measuremnt-Objekt zurückgeben
        return {
            "sensor_id": sensor_id,
            "location": location,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
        }
