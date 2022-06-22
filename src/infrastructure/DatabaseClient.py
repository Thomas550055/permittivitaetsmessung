#!/usr/bin/python
# define connection and cursor
import sqlite3


class DatabaseClient:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)

    def create_measurements_table(self):
        cursor = self.connection.cursor()
        create_measurements_table = """
            CREATE TABLE IF NOT EXISTS measurement(
                ID INTEGER PRIMARY KEY,
                MaterialName TEXT,
                Temperature  REAL,
                Humidity REAL,
                MaterialType TEXT,
                SerialNumber TEXT,
                SampleThickness REAL,
                MeasurementStarted DATETIME
            )
        """
        cursor.execute(create_measurements_table)
        self.connection.commit()

    def close_database_connection(self):
        self.connection.close()



