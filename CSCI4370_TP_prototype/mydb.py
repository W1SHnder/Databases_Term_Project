# Install Mysql on computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Thoughts")

print("Database Created")