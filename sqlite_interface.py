# Stephen McDonnell
# 24/04/2019

import sqlite3

class SqliteInterface:

    # Initialise Database
    def __init__(self, conn, identifier):
        print("SQLite Connector: " + identifier)
        print("SQLITE_THREADING_MODE_ENABLED: " + str(sqlite3.threadsafety))
        self.sql_connection = None
        self.create_connection(conn)
        self.create_table()
        self.delete_all()
        self.prefill()
        self.index = 1

    # Create connection to SQLite DB
    def create_connection(self, db_file):
        try:
            self.sql_connection = sqlite3.connect(db_file)
        except Exception as e:
            print(e)
        return None

    # Create a table in an SQLite DB
    def create_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS readings (
                        id integer PRIMARY KEY,
                        temperature real,
                        pressure real,
                        humidity real
                  ); """
        try:
            cursor = self.sql_connection.cursor()
            cursor.execute(sql)
        except Exception as e:
            print(e)

    # Insert a new value into an SQLite DB
    def insert(self, args):
        sql = """INSERT INTO readings(temperature, pressure, humidity)
                 VALUES(?,?,?) """
        try:
            cursor = self.sql_connection.cursor()
            cursor.execute(sql, tuple(args))
            self.sql_connection.commit()
        except Exception as e:
            print(e)

    # Prefill DB with null values so only updating is needed
    def prefill(self):
        for _ in range(1, 100):
            self.insert([None, None, None])

    # Update a pre-existing value within a SQLite DB table
    def update(self, args):
        sql = """UPDATE readings
                 SET  temperature = ? ,
                      pressure = ? ,
                      humidity = ?
                 WHERE id = ?
                 """
        args = (*args, self.index)
        cursor = self.sql_connection.cursor()
        cursor.execute(sql, args)
        self.sql_connection.commit()
        self.index += 1
        if self.index >= 101:
            self.index = 1

    # Delete all current entries in a SQLite DB, resetting it
    def delete_all(self):
        sql = "DELETE FROM readings"
        cursor = self.sql_connection.cursor()
        cursor.execute(sql)
        self.sql_connection.commit()

    # Query entries at a particular index
    def query_id(self, query_id):
        cursor = self.sql_connection.cursor()
        cursor.execute("SELECT * FROM readings WHERE id=?", (query_id,))

        return cursor.fetchall()


    # Return all entries in the table
    def query_all(self):
        cursor = self.sql_connection.cursor()
        cursor.execute("SELECT * FROM readings")

        return cursor.fetchall()

