'''special case you can specify table name as memory to create a database in RAM instead of a database on disk'''
import sqlite3

conn = sqlite3.connect('votercard.db')
c = conn.cursor()

def dell():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS VC")
    print("Table Dropped")

def tabb():
    conn.execute("CREATE TABLE IF NOT EXISTS VC (vid VARCHAR PRIMARY KEY NOT NULL , age INT NOT NULL ,vcast INT NOT NULL)")
    print("Table Created")

def inss():
    #no=int(input("No. of Data to be entered : "))
    #for i in range(no):
    a=input("Voter Id")
    a=a.upper()
    b=input("Age ")
    conn.execute("INSERT INTO VC VALUES (?,?,0)",(a,b))
    conn.commit()

def showw():
    c = conn.cursor()
    c.execute('SELECT * FROM VC')
    for row in c.fetchall():
        print("Voter Id ",row[0])
        print("Age ",row[1])
        print("Vote Casted [0=No/1=Yes] ",row[2])

    print("\n")

def po():
    print("1.Create Table\n2.Show Table\n3.Insert New Values in Table\n4.Delete Existing Table\n")
    n=int(input("Enter Option "))
    while(n!=0):
        if (n == 1):
            tabb()
        if (n == 2):
            showw()
        if (n == 3):
            inss()
        if (n == 4):
            dell()
        n = int(input('Enter 0 to end '))

po()
