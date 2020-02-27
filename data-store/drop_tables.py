import sqlite3

conn = sqlite3.connect('readings.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE residence_details
          ''')
c.execute('''
          DROP TABLE future_residence_details
          ''')

conn.commit()
conn.close()
