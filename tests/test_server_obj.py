import os
import sys
sys.path.insert(0, os.getcwd()) 

import pytest
from mysql.connector import Error
import server_obj
import mysql.connector

class TestServerFunctions():
    def test_init(self):
        s = server_obj.ServerObj()
        assert (type(s.connection) == mysql.connector.connection_cext.CMySQLConnection)

    def test_read_query(self):
        s = server_obj.ServerObj()
        res = s.read_query(s.connection, 'SHOW DATABASES')
        print(res)
        assert (type(res) == list)
        assert (type(res[0]) == tuple)

    def test_create_database1(self):
        s = server_obj.ServerObj()
        before = len(s.read_query(s.connection, 'SHOW DATABASES;'))
        s.edit_databases("""CREATE DATABASE test_db;""")
        after = len(s.read_query(s.connection, 'SHOW DATABASES;'))
        assert ((after - before) == 1)

    def test_db_connection(self):
        s = server_obj.ServerObj()
        s.create_db_connection('test_db')
        assert (type(s.db_connection) == mysql.connector.connection_cext.CMySQLConnection)

    def test_add_record_to_database(self):
        s = server_obj.ServerObj()
        s.create_db_connection('test_db')
        s.execute_query(s.db_connection, """USE test_db;""")
        s.execute_query(s.db_connection, """
            CREATE TABLE TestTable (
                id int NOT NULL AUTO_INCREMENT, 
                name VARCHAR(10) NOT NULL, 
                year int NOT NULL, 
                PRIMARY KEY(id));""")
        s.execute_query(s.db_connection, """
            INSERT INTO TestTable (id, name, year)
                VALUES (1, "john", 2000);
            """)
            
        res = s.read_query(s.db_connection, """
            SELECT * FROM TestTable""")
        assert (res[0] == (1, 'john', 2000))

    #Add another test for when I figure out what format I'm going to input the data from python

    
    def test_remove_database(self):
        s = server_obj.ServerObj()
        before = len(s.read_query(s.connection, 'SHOW DATABASES'))
        s.edit_databases("DROP DATABASE test_db")
        after = len(s.read_query(s.connection, 'SHOW DATABASES'))
        assert ((before - after) == 1)
