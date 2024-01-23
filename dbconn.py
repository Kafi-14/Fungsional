import pymysql

conn = pymysql.connect(
    host="sql6.freesqldatabase.com",
    database="sql6679140",
    user="sql6679140",
    password="68tnEMKUJZ",
    # charset
    cursorclass=pymysql.cursors.DictCursor,
)

cursor = conn.cursor()

sql = """ Create Table game2 (
    id integer PRIMARY KEY AUTO INCREMENT,
    nama text NOT NULL,
    genre text NOT NULL,
    rating text NOT NULL)
"""

cursor.execute(sql)
conn.close()
