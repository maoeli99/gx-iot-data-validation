# gx-iot-data-validation

## Beschreibung
Dieses Projekt demonstriert die Implementierung einer automatisierten Datenvalidierung für IoT-Daten mit dem Open-Source-Framework [Great Expectations (GX)](https://greatexpectations.io/). Die Fallstudie basiert auf der Generierung synthetischer Wetterdaten, die in einer PostgreSQL-Datenbank gespeichert und anschließend mit GX validiert werden. 

Diese README-Datei führt Schritt für Schritt durch die Installation und Ausführung des Projekts.

---
## Installation und Ausführung

### **Schritt 1: Installation der Projektabhängigkeiten**
Zunächst müssen alle erforderlichen Abhängigkeiten installiert werden. Diese sind in der Datei `requirements.txt` aufgelistet und können mit folgendem Befehl installiert werden:

```sh
pip install -r requirements.txt
```

Dadurch werden u. a. folgende Hauptkomponenten installiert:
- **Great Expectations (GX)** zur Datenvalidierung
- **SQLAlchemy** zur Datenbankanbindung
- **Pandas & NumPy** für die Datenverarbeitung
- **FastAPI & Uvicorn** zur webbasierten Bereitstellung der Validierungsergebnisse

---
### **Schritt 2: Aufsetzen einer PostgreSQL-Datenbank**
Das Projekt nutzt eine PostgreSQL-Datenbank zur Speicherung der generierten Sensordaten. Die Datenbank muss mit folgender Konfiguration aufgesetzt werden:

```
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_NAME = "postgres"
```

Falls PostgreSQL noch nicht installiert ist, kann alternativ ein Docker-Container verwendet werden. Hierzu muss Docker auf dem lokalen System bereits installiert sein.

```sh
docker run -d --name my_postgres_container \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=postgres \
    -p 5432:5432 postgres:latest
```

Dieser Befehl startet eine PostgreSQL-Datenbank in einem Docker-Container mit den oben genannten Zugangsdaten.

---
### **Schritt 3: Ausführung des Skripts `db_setup.py`**
Sobald das Datenbanksystem bereit ist, muss das Datenbankschema eingerichtet werden. Dies erfolgt durch das folgende Skript:

```sh
python db_setup.py
```

#### **Was macht `db_setup.py`?**
- Stellt eine Verbindung zur PostgreSQL-Datenbank her
- Erstellt die Tabelle `measurement`, falls sie noch nicht existiert
- Definiert das Schema für die Speicherung der Sensordaten (u. a. Zeitstempel, Sensor-ID, Messwerte für Temperatur, Luftfeuchtigkeit und Windgeschwindigkeit)
- Schreibt einen Test-Datensatz in die Datenbank, um die Funktionsweise zu prüfen

---
### **Schritt 4: Erstellung einer lokalen GX-Umgebung**
Um eine lokale GX-Umgebung zu erzeugen, muss das Jupyter-Notebook `gx_setup.ipynb` vollständig ausgeführt werden.

#### **Was macht `gx_setup.ipynb`?**
- Initialisiert den Great Expectations Data Context
- Verbindet GX mit der PostgreSQL-Datenbank
- Definiert eine Expectation Suite mit Regeln zur Datenvalidierung
- Erstellt einen Checkpoint zur zyklischen Validierung der eingehenden Sensordaten

Das Notebook kann über Jupyter geöffnet und schrittweise ausgeführt werden:

```sh
jupyter notebook gx_setup.ipynb
```

---
### **Schritt 5: Ausführung des Skripts `generator.py`**
Nun kann die Generierung von Sensordaten gestartet werden:

```sh
python generator.py
```

#### **Was macht `generator.py`?**
- Simuliert Sensordaten für eine Wetterstation
- Generiert zufällige Messwerte für Temperatur, Luftfeuchtigkeit und Windgeschwindigkeit
- Integriert absichtlich fehlerhafte Messwerte, um die Datenvalidierung zu testen
- Speichert die Daten fortlaufend in die PostgreSQL-Datenbank

---
### **Schritt 6: Ausführung des Skripts `validator.py`**
Nachdem die Sensordaten generiert werden, kann die Validierung gestartet werden:

```sh
python validator.py
```

#### **Was macht `validator.py`?**
- Führt die in `gx_setup.ipynb` definierten Validierungsregeln aus
- Nutzt den Checkpoint zur systematischen Prüfung der eingehenden Daten
- Erstellt automatische Validierungsberichte (`Data Docs`), die in einem Webbrowser betrachtet werden können
- Zeigt die Ergebnisse in einer grafischen Oberfläche an, um Datenqualitätsprobleme zu erkennen

Die Validierungsergebnisse können anschließend unter folgender Adresse im Browser geöffnet werden:

```sh
http://localhost:8000
```
---

