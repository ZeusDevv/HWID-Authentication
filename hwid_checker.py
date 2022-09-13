import subprocess
import pymysql as MySQLdb
import time
import os
from sys import stderr, stdin, stdout, platform

# SQL
#
# CREATE TABLE IF NOT EXISTS DB_NAME (HWID TEXT)
#


def hwidcheck():
    if platform == "linux" or platform == "linux2":
        try:
            db = MySQLdb.connect(
                    host='IP',
                    user='username',
                    passwd='dbpassword',
                    db="db-name"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM db-name")
            rows = cursor.fetchall()
            for row in rows:
                hw = str(subprocess.check_output(['sudo','cat','/sys/class/dmi/id/product_uuid']).decode().strip())
            
                hwid = row[0]
                if hw in hwid:
                    print("Authenticated\nPlease Wait.")
                    time.sleep(2)
                    os.system("clear")
                    # Function here
                elif hw not in hwid:
                    print(f"you're either not whitelisted or your HWID Has Changed")

        except MySQLdb.Error:
            print ("Failed to connect to server, make sure you're connected to the internet!")
            return

    elif platform == "win32":
        current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        try:
            db = MySQLdb.connect(
                    host='IP',
                    user='username',
                    passwd='dbpassword',
                    db="db-name"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM db-name")
            data = cursor.fetchall()
            
            for x in data:
                hwid = x[0]
                if current_machine_id in hwid:
                    print("Authenticated\nPlease Wait.")
                    time.sleep(2)
                    os.system("clear")
                    # Function here
                else:
                    print(f"you're either not whitelisted or your HWID Has Changed")
        except MySQLdb.Error:
            print ("Failed to connect to server, make sure you're connected to the internet!")
            return