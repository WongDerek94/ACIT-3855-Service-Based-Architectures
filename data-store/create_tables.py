import sqlite3

conn = sqlite3.connect('events.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE residence_details
          (id INTEGER PRIMARY KEY ASC, 
           user_id VARCHAR(250) NOT NULL,
           user_name VARCHAR(250) NOT NULL,
           residence_type VARCHAR(100) NOT NULL,
           phone_num VARCHAR(100) NOT NULL,
           capacity INTEGER NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE future_residence_details
           (id INTEGER PRIMARY KEY ASC, 
           user_id VARCHAR(250) NOT NULL,
           user_name VARCHAR(250) NOT NULL,
           residence_type VARCHAR(100) NOT NULL,
           phone_num VARCHAR(100) NOT NULL,
           capacity INTEGER NOT NULL,
           date VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

conn.commit()
conn.close()
