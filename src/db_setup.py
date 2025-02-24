import psycopg2
from psycopg2 import OperationalError
from constants import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD


def connect():
    """
    Stellt eine Verbindung zur PostgreSQL-Datenbank her und gibt das Verbindungsobjekt zurück.
    """
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
        print(f"Fehler bei der Verbindung zur Datenbank: {e}")
        return None


def create_measurement_table(conn):
    """
    Erstellt die Tabelle 'measurement' in der Datenbank, falls sie nicht existiert.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS measurement (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        sensor_id TEXT,
        location TEXT,
        temperature DOUBLE PRECISION,
        humidity DOUBLE PRECISION,
        pressure DOUBLE PRECISION,
        wind_speed DOUBLE PRECISION,
        wind_direction DOUBLE PRECISION
    );
    """
    try:
        with conn.cursor() as cur:
            cur.execute(create_table_query)
            conn.commit()
            print(
                "Tabelle 'measurement' wurde erfolgreich erstellt oder existiert bereits."
            )
    except Exception as e:
        print(f"Ein Fehler ist beim Erstellen der Tabelle aufgetreten: {e}")


def insert_sample_data(conn):
    """
    Fügt einen Beispieldatensatz in die Tabelle 'measurement' ein.
    """
    insert_data_query = """
    INSERT INTO measurement (sensor_id, location, temperature, humidity, pressure, wind_speed, wind_direction)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    sample_data = (
        "WS_001",  # sensor_id
        "Berlin",  # location
        22.5,  # temperature
        45.0,  # humidity
        1013.25,  # pressure
        5.5,  # wind_speed
        180.0,  # wind_direction
    )
    try:
        with conn.cursor() as cur:
            cur.execute(insert_data_query, sample_data)
            conn.commit()
            print("Beispieldatensatz wurde erfolgreich eingefügt.")
    except Exception as e:
        print(f"Ein Fehler ist beim Einfügen des Datensatzes aufgetreten: {e}")


# Routine starten
conn = connect()
if conn:
    create_measurement_table(conn)
    insert_sample_data(conn)
    conn.close()
