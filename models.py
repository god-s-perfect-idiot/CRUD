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
                sender VARCHAR(255) NOT NULL,
                recipent VARCHAR(255) NOT NULL,
                credits INT NOT NULL
                )ENGINE = INNODB"""

        self.cursor.execute(query)
        self.connection.commit()


class ManageUser:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',database='tsf',user='root',password='root')
            if(self.connection.is_connected()):
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()

        except Error as e:
            print("Error connection to db",e)

    def getuserlist(self):
        query = "SELECT * FROM user;"
        result = self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def getuserdetails(self,id):
        query = "SELECT * FROM user WHERE user_id="+str(id)+";"
        result = self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def updatecreds(self,id1,id2,crd):
        query = "UPDATE user SET credit=credit-"+str(crd)+" WHERE user_id="+str(id1)+";"
        print(query)
        result = self.cursor.execute(query)
        results = self.cursor.fetchone()
        self.connection.commit()

        query = "UPDATE user SET credit=credit+"+str(crd)+" WHERE user_id="+str(id2)+";"
        result = self.cursor.execute(query)
        results = self.cursor.fetchone()
        self.connection.commit()


class ManageTrs:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',database='tsf',user='root',password='root')
            if(self.connection.is_connected()):
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()

        except Error as e:
            print("Error connection to db",e)

    def addtrn(self,id1,id2,name1,name2,crd):
        query = "INSERT INTO transfers(sender_id,recipient_id,sender,recipent,credits) VALUES("+str(id1)+","+str(id2)+",'"+name1+"','"+name2+"',"+str(crd)+");"
        result = self.cursor.execute(query)
        results = self.cursor.fetchone()
        self.connection.commit()

    def gettrn(self,id):
        query = "SELECT * FROM transfers WHERE sender_id="+str(id)+" OR recipient_id="+str(id)+";"
        result = self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
