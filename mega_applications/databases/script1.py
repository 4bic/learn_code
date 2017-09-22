import sqlite3

def create_table():
    # coonect to db
    conn = sqlite3.connect("lite.db")
    # create a cursor object
    cur=conn.cursor()
    # execute db creation
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # commit to db
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    # connect to db
    conn = sqlite3.connect("lite.db")
    # create a cursor object
    cur=conn.cursor()
    # add data
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    # commit to db
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

delete("Milk")
print (view())
