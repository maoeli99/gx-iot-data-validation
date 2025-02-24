import random
import psycopg2
from psycopg2 import OperationalError
import time
from datetime import datetime
from sensor import Sensor
from constants import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD, CYCLE_TIME

# Liste mit verfügbaren Sensoren
sensors = [
    Sensor("WS_001", "Berlin"),
    Sensor("WS_002", "Hamburg"),
    Sensor("WS_003", "München"),
    Sensor("WS_004", "Köln"),
    Sensor("WS_005", "Frankfurt"),
]


def connect():
    """Stellt eine Verbindung zur PostgreSQL-Datenbank her und gibt das Verbindungsobjekt zurück."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
        )
        return conn

    except OperationalError as e:
        return None  # Rückgabe von None, falls die Verbindung fehlschlägt


def insert_measurement(measurement):
    """Schreibt das übergebene Measurement-Objekt in die Datenbank"""
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO measurement (timestamp, sensor_id, location, temperature, humidity, pressure, wind_speed, wind_direction) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                datetime.now(),
                measurement["sensor_id"],
                measurement["location"],
                measurement["temperature"],
                measurement["humidity"],
                measurement["pressure"],
                measurement["wind_speed"],
                measurement["wind_direction"],
            ),
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Fehler beim Einfügen in die DB: {e}")


def generate_data():
    """
    Startet die Simulation.

    Diese Funktion wählt zufällig einen Sensor aus der Liste 'sensors' aus, generiert eine Messung
    und speichert die Daten in der Datenbank. Zwischen den Messungen wird eine Pause von 'CYCLE_TIME'
    Sekunden eingelegt. Die Simulation läuft ununterbrochen, bis sie manuell durch eine Tastenkombination
    (z.B. STRG+C) gestoppt wird.

    Ausnahme:
        KeyboardInterrupt: Wird ausgelöst, wenn die Simulation manuell vom Benutzer gestoppt wird.
    """
    print("Simulation gestartet (STRG+C zum Stoppen)")
    try:
        while True:
            sensor = random.choice(sensors)  # Zufällige Wetterstation auswählen
            measurement = sensor.generate_measurement()  # Sensordaten generieren
            insert_measurement(measurement)  # In Datenbank speichern
            time.sleep(CYCLE_TIME)  # Pause
    except KeyboardInterrupt:
        print("\nSimulation gestoppt.")


# Routine starten
generate_data()
