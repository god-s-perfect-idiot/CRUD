import mysql.connector
from mysql.connector import Error

class Schema:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',database='tsf',user='root',password='root')
            if(self.connection.is_connected()):
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
            self.create_user_table()
            self.create_transfers_table()


        except Error as e:
            print("Error connection to db",e)

    def create_user_table(self):
        query = """CREATE TABLE IF NOT EXISTS user(
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                Age INT NOT NULL,
                email VARCHAR(255) NOT NULL,
                credit INT NOT NULL
                ) ENGINE = INNODB;
                """
        self.cursor.execute(query)
        self.connection.commit()

    def create_transfers_table(self):
        query = """CREATE TABLE IF NOT EXISTS transfers(
                trn_id INT AUTO_INCREMENT PRIMARY KEY,
                sender_id INT NOT NULL,
                recipient_id INT NOT NULL,
                credits INT NOT NULL
                )ENGINE = INNODB"""

        self.cursor.execute(query)
        self.connection.commit()


class Manage:
    table = 
