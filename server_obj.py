import mysql.connector
from mysql.connector import Error
import pandas as pd
import configparser

class ServerObj:
    def __init__(self):
        self.read_config()
        self.connection = self.create_server_connection()
        return

    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read("configurations.ini")
        return

    def create_server_connection(self):
        connection = None       #Closes existing connections
        try:
            connection = mysql.connector.connect(
                host=self.config["SQLServerSettings"]["host_name"],
                user=self.config["SQLServerSettings"]["user_name"],
                passwd=self.config["SQLServerSettings"]["user_password"]
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection

serverObj = ServerObj()