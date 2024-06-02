from datetime import datetime
import mysql.connector

class Connector:
    """
    Provides a streamlined interface for connecting to the MySQL Workbench/database.

    Attributes:
        None

    Methods:
        create_database_connection: Establishes a secure connection to the MySQL Workbench.
        open_connection: opens the connection to Saturn's SQL database.
        close_connection: closes the connection to Saturn's SQL database.
        init_playlist: Initializes tables found in our database.
        cleanup_database: updates database and removes sounds that aren't in the sounds directory.
    """

    def __init__(self):
        self.cnx = None
        self.cursor = None
        # self.connect_to_my_sql()


    def open_connection(self):
        config = {
            "user": "root",
            "password": "!WhitmanMemo08?",
            "port": 3307,
            "database": "FamilyTree",
            "raise_on_warnings": True,
        }

        try:
            self.cnx = mysql.connector.connect(**config)
            self.cursor = self.cnx.cursor()
            
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("Could not connect to MySQL:", err)


    def close_connection(self):
        self.cnx.close()
        self.cursor.close()

if __name__ == "__main__":
    db = Connector()
    db.open_connection()
    db.close_connection()