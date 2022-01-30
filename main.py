import csv
import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': '23bodIf3FyslAkbM',
    'host': '35.192.1.42',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
}

config['database'] = 'ensoccerpedia'

# now we establish our connection
cnxn = mysql.connector.connect(**config)

cursor = cnxn.cursor(buffered=True)  # initialize connection cursor

season = input("Please enter the season year (i.e. for 2018-19 season enter 2018): ")
home = input("Please enter the home team: ")
away = input("Please enter the away team: ")

cursor.execute("""
    SELECT * FROM engsoccerdata
    WHERE Home = %s 
    AND Visitor = %s
    AND Season = %s""", (home, away, season))

for row in cursor:
    date = row[0]
    home = row[2]
    visitor = row[3]
    hgoal = row[5]
    agoal = row[6]
    
    print("Game Info: ")
    print("Date: " + date)
    print("Teams: " + home + " - " + visitor)
    print("Result: " + str(hgoal) + "-" + str(agoal))
    
cursor.close()

cursor = cnxn.cursor(buffered=True)

cnxn.commit()
cnxn.close()
