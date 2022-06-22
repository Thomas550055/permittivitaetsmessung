#!/usr/bin/python
# define connection and cursor
import sqlite3

# TODO: replace this with shared database
databasePath = '../permittivity.db'

connection = sqlite3.connect(databasePath)

cursor = connection.cursor()

createMeasurementsTable = """
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

cursor.execute(createMeasurementsTable)

connection.commit()
connection.close()
