import sqlite3

## Connecting to sqlite
connection = sqlite3.connect("player.db")

## Create a cursor object to insert,create, retrieve
cursor = connection.cursor()

## Create table
table_info="""
Create table PLAYER(NAME VARCHAR(25), CLUB VARCHAR(25),
COUNTRY VARCHAR(25),GOALS INT);

"""

# cursor.execute(table_info)

## Insert records

cursor.execute(''' Insert into PLAYER values('Messi','Inter Miami','Argentina',850) ''')
cursor.execute(''' Insert into PLAYER values('Ronaldo','Al Nassar','Portugal',910) ''')
cursor.execute(''' Insert into PLAYER values('Neymar','Al Hilal','Brazil',500) ''')
cursor.execute('''INSERT INTO PLAYER VALUES('Mbappe', 'PSG', 'France', 420)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Lewandowski', 'Barcelona', 'Poland', 630)''')
cursor.execute('''INSERT INTO PLAYER VALUES('De Bruyne', 'Manchester City', 'Belgium', 290)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Modric', 'Real Madrid', 'Croatia', 450)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Salah', 'Liverpool', 'Egypt', 370)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Vinicius Jr.', 'Real Madrid', 'Brazil', 180)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Haaland', 'Manchester City', 'Norway', 150)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Son Heung-min', 'Tottenham', 'South Korea', 230)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Griezmann', 'Atletico Madrid', 'France', 310)''')
cursor.execute('''INSERT INTO PLAYER VALUES('Rashford', 'Manchester United', 'England', 170)''')

## Displaying Records
print("Inserted data are")
data = cursor.execute(''' Select * from PLAYER ''')
for row in data:
    print(row)

## Close connection
connection.commit()
connection.close()