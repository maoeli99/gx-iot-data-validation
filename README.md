# gx-iot-data-validation

## Beschreibung
Dieses Projekt demonstriert die Implementierung einer automatisierten Datenvalidierung für IoT-Daten mit dem Open-Source-Framework [Great Expectations (GX)](https://greatexpectations.io/). Die Fallstudie basiert auf der Generierung synthetischer Wetterdaten, die in einer PostgreSQL-Datenbank gespeichert und anschließend mit GX validiert werden. 

Diese README-Datei führt Schritt für Schritt durch die Installation und Ausführung des Projekts.

---
## Installation

### Verwendetes OS: **Windows 11** (alle nachfolgenden Befehle gelten ausschließlich für Windows-Systeme)
### Verwendete Python-Version: **3.11.3**

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

Es empfiehlt sich, eine virtuelle Umgebung (venv) im Root-Verzeichnis des Projekts (./gx-iot-data-validation-main) anzulegen und dort die Projektabhängigkeiten zu installieren:

Erstellen der virtuellen Umgebung:

```sh
py -m venv .venv
```
Aktivieren der virtuellen Umgebung:

```sh
.venv\Scripts\activate
```

Anschließend pip install ausführen.

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

## Ausführung

### Wichtiger Hinweis

Alle Skripte in diesem Projekt müssen **aus dem Verzeichnis `src` heraus** ausgeführt werden, da sie relative Pfade verwenden. Andernfalls kann es zu Fehlern beim Laden von Dateien oder Modulen kommen.  

---
### **Schritt 1: Ausführung des Skripts `db_setup.py`**
Sobald das Datenbanksystem bereit ist, muss das Datenbankschema eingerichtet werden. Dies erfolgt durch das folgende Skript:

```sh
py db_setup.py
```

#### **Was macht `db_setup.py`?**
- Stellt eine Verbindung zur PostgreSQL-Datenbank her
- Erstellt die Tabelle `measurement`, falls sie noch nicht existiert
- Definiert das Schema für die Speicherung der Sensordaten
- Schreibt einen Test-Datensatz in die Datenbank, um die Funktionsweise zu prüfen

---
### **Schritt 2: Erstellung einer lokalen GX-Umgebung**
Um eine lokale GX-Umgebung zu erzeugen, muss das Jupyter-Notebook `gx_setup.ipynb` vollständig ausgeführt werden.

#### **Was macht `gx_setup.ipynb`?**
- Initialisiert den Great Expectations Data Context
- Verbindet GX mit der PostgreSQL-Datenbank
- Definiert eine Expectation Suite mit Regeln zur Datenvalidierung
- Erstellt einen Checkpoint zur zyklischen Validierung der eingehenden Sensordaten

---
### **Schritt 3: Ausführung des Skripts `generator.py`**
Nun kann die Generierung von Sensordaten gestartet werden:

```sh
py generator.py
```

#### **Was macht `generator.py`?**
- Simuliert Sensordaten für eine Wetterstation
- Generiert zufällige Messwerte für Temperatur, Luftfeuchtigkeit und Windgeschwindigkeit
- Integriert absichtlich fehlerhafte Messwerte, um die Datenvalidierung zu testen
- Speichert die Daten fortlaufend in die PostgreSQL-Datenbank

#### **Hinweis zur Nutzung des Generators**
Nach dem Start des Generators wird das darunterliegende Terminal blockiert. Weitere Skripte müssen in einem neuen Terminal gestartet werden. Der Generator kann jederzeit mit **Strg + C** beendet werden.

---
### **Schritt 4: Ausführung des Skripts `validator.py`**
Nachdem die Sensordaten generiert werden, kann die Validierung gestartet werden:

```sh
py validator.py
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
#### **Hinweis zur Nutzung des Validators**
Nach dem Start des Validators wird das darunterliegende Terminal blockiert. Weitere Skripte müssen in einem neuen Terminal gestartet werden. Der Validator kann jederzeit mit **Strg + C** beendet werden.

---

