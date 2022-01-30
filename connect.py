# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:08:39 2022

@author: mvera
"""

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

cursor = cnxn.cursor()  # initialize connection cursor

# cursor.execute('CREATE DATABASE ensoccerpedia')  # create a new 'testdb' database
# cnxn.close()  # close connection because we will be reconnecting to testdb

# cursor.execute("CREATE TABLE engsoccerdata ("
#                "Date VARCHAR(255),"
#                "Season INT(255),"
#                "Home TEXT(21845),"
#                "Visitor TEXT(21845),"
#                "FT VARCHAR(255),"
#                "hgoal INT(255),"
#                "agoal INT(255),"
#                "League VARCHAR(255) )")

data = 'engsoccerdata.csv'

query = (
    "INSERT INTO engsoccerdata(Date, Season, Home, Visitor, FT, hgoal, agoal, League)"
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
)

with open(data, mode='r') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    csv_data_list = list(reader)
    i = 0
    for row in csv_data_list:
        cursor.execute(query, row)
        i+=1
        if i % 100 == 0:
            print(i)

cnxn.commit()
cursor.close()
cnxn.close()
print("Done")