import sqlite3

#Opret forbindelse til database (eller en ny hvis den ikke findes)
conn = sqlite3.connect('members.db')
cursor = conn.cursor()

#Opret tabel hvis den ikke findes
cursor.execute('''
                CREATE TABLE IF NOT EXISTS 
                member (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                gender TEXT NOT NULL,
                email TEXT NOT NULL,
                phonenumber TEXT NOT NULL,
                address TEXT NOT NULL,
                nationality TEXT NOT NULL,
                active BOOLEAN NOT NULL,
                github_username TEXT NOT NULL
                )
                ''')

#Gem ændringer og luk forbindelsen
conn.commit()
conn.close()
