# define connection and cursor
import sqlite3


class DatabaseClient:
    def __init__(self, database_path):
        # initialize database connection & store open connection as class member variable
        self.connection = sqlite3.connect(database_path)

        # create material measurement and fds row table => IF NOT EXISTS
        # we do this in the __init__ method because every database client needs those tables
        # in order to work
        self.__create_material_measurement_table()
        self.__create_fds_row_table()

    def __create_material_measurement_table(self):
        cursor = self.connection.cursor()
        create_material_measurement_table = """
            CREATE TABLE IF NOT EXISTS MaterialMeasurement(
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
        cursor.execute(create_material_measurement_table)
        self.connection.commit()

    # TODO: create column names for FDS Table values
    def __create_fds_row_table(self):
        cursor = self.connection.cursor()
        create_fds_row_table = """
            CREATE TABLE IF NOT EXISTS FDSRow(
                ID INTEGER PRIMARY KEY,
                MeasurementID INTEGER,
                Frequency REAL,

                FOREIGN KEY (MeasurementID) REFERENCES Measurement(ID)
            )
        """
        cursor.execute(create_fds_row_table)
        self.connection.commit()

    def close_database_connection(self):
        self.connection.close()



