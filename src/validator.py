import great_expectations as gx
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import threading
import time
from constants import CHECKPOINT_NAME, INTERVAL_SECONDS

# GX-Context initialisieren
context = gx.get_context(mode="file")

checkpoint = context.checkpoints.get(CHECKPOINT_NAME)

# FastAPI-App erstellen
app = FastAPI()

# Verzeichnis, in dem index.html und alle zugehörigen Data Docs liegen
DATA_DOCS_DIR = os.path.abspath("./gx/uncommitted/data_docs/local_site")

# Statische Dateien mounten:
# Mit html=True wird automatisch index.html als Startseite geladen.
app.mount("/", StaticFiles(directory=DATA_DOCS_DIR, html=True), name="data_docs")


def run_checkpoint_periodically(interval):
    """Führt den Checkpoint in einem separaten Thread alle `interval` Sekunden aus."""
    while True:
        try:
            print("Validierung gestartet")
            checkpoint.run()
            print("Validierung erfolgreich ausgeführt.")
        except Exception as e:
            print(f"Fehler bei der Validierung: {e}")
        time.sleep(interval)


# Thread für die periodische Checkpoint-Ausführung starten
thread = threading.Thread(target=run_checkpoint_periodically, args=(INTERVAL_SECONDS,))
thread.daemon = True
thread.start()

# FastAPI-Server starten
uvicorn.run(app, host="0.0.0.0", port=8000)
