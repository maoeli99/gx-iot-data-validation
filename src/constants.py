# Datenbank-Konstanten
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_NAME = "postgres"
DB_TABLE = "measurement"

# GX-Konstanten
DATA_SOURCE = "postgres_weather_db"
DATA_ASSET = "measurement"
BATCH_DEFINITION = "last_day_batch"
EXPECTATION_SUITE = "weather_data_expectation_suite"
VALIDATION_DEFINITION = "weather_data_validation_definition"
CHECKPOINT_NAME = "weather_data_validation_checkpoint"
INTERVAL_SECONDS = 86400
CYCLE_TIME = 1
