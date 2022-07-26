import mysql.connector
from mysql.connector import Error
import pandas as pd
import configparser

class ServerObj:
    def __init__(self):
        self.read_config()
        self.var2 = 3
        self.connection = self.create_server_connection()
        return

    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read("/Users/emilywidjaja/Documents/Coder/uni_app/configurations.ini") #THIS LINE HAS TO BE UPDATED
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

    def edit_databases(self, query):
    #Creates database
        cursor = self.connection.cursor() #Creates cursor object
        try:
            cursor.execute(query)   #Executes query in the server via connection 
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
        return
    
    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit() #Makes sure commands are implemented
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    
    def create_db_connection(self, db_name):
    #Multiple databases possible on server. Connects to correct database
        connection = None
        try:
            self.db_connection = mysql.connector.connect(
                host=self.config["SQLServerSettings"]["host_name"],
                user=self.config["SQLServerSettings"]["user_name"],
                passwd=self.config["SQLServerSettings"]["user_password"],
                database=db_name
            )
            print("MySQL Database connection successful.")
        except Error as err:
            print(f"Error: '{err}'")
        return

    def read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

# serverObj = ServerObj()
# print(serverObj.read_query(serverObj.connection, "SHOW DATABASES"))
# serverObj.create_db_connection('test_db')
# #serverObj.execute_query(serverObj.db_connection, """
# # CREATE TABLE TestTable (
# #     id int NOT NULL AUTO_INCREMENT, 
# #     name VARCHAR(10) NOT NULL, 
# #     year int NOT NULL, 
# #     PRIMARY KEY(id));""")
# serverObj.execute_query(serverObj.db_connection, """INSERT INTO TestTable VALUES (4, 'trina', 1989);""")
# res = serverObj.read_query(serverObj.db_connection, "SELECT * FROM TestTable;")
# serverObj.edit_databases("DROP DATABASE test_db;")