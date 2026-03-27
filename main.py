import mysql.connector
from abc import ABC, abstractmethod
#///////////////////////////////////////////////////////////////////////////////////////////
                                    #normal function
def line():
    print("/"*80)

#/////////////////////////////////////////////////////////////////////////////////////////////////////
                                    #sql operation

        #db connection


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
        #cursor
mycursor = mydb.cursor()
    #show all records
def show():
    mycursor.execute("SELECT * FROM friend")
    result = mycursor.fetchall()
    if len(result) == 0:
        print("no records find in the 'friend' table!")
    else:
        for index, frd in enumerate(result):
            print(f"friend {index+1}:")
            print(f"Name: {frd[0]}  | gender: {frd[1]}  | relation: {frd[2]}")
            print("="*80)
    line()
                                    

    #database
class Database(ABC):
    def __init__(self, name="myself"):
        self.name = name
        #create
    def create():
        mycursor.execute("CREATE DATABASE IF NOT EXISTS myself")
        mycursor.execute("USE myself")
        mycursor.execute("CREATE TABLE IF NOT EXISTS friend( name varchar(100) not null, gender enum('M', 'F') not null, relation varchar(100) not null)")
        print("Database:    myself; successful create!")
        print("Table:       friend; successful create!")
    @abstractmethod
    def insert(self):
        return NotImplemented
    def clearTB(self, table):
        query = "DROP TABLE %s"
        mycursor.execute(query, table)

    #friend
class Friend(Database):
    def __init__(self, name, gender, relation):
        super().__init__(name)
        self.name = name
        self.gender = gender
        self.relation = relation
    def insert(self):
        query = "INSERT INTO friend VALUES (%s, %s, %s)"
        mycursor.execute(query, (self.name, self.gender, self.relation))
        mydb.commit()
        print(f"name:{self.name} | gender:{self.gender} | relation:{self.relation}, is inserted into the database")
        line()

if __name__ == "__main__":
        #elements
    list_frds = list()
        #information
    line()
    Database.create()
    line()
        #main function
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        while True:
                    #menu
            print(".", "-"*24, ".")
            print("|", "1", "-"*10, "insert     ", "|")
            print("|", "2", "-"*10, "show all   ", "|")
            print(".", "-"*24, ".")
            choice = int(input(": "))
            line()
            if choice == 1:
                name = input("NAME: ")
                gender = input("GENDER(M/ F): ")
                relationship = input("RELATION: ")
                line()
                Friend(name, gender, relationship).insert()
            elif choice == 2:
                show()
    except mysql.connector.Error as e:
        print(e)

