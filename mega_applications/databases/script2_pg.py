import psycopg2

def create_table():
    # coonect to db
    conn = psycopg2.connect(dbname='mega_app', user='4bic',password='postgres', host='localhost', port='5432')
    # create a cursor object
    cur=conn.cursor()
    # execute db creation
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # commit to db
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    # connect to db
    conn = psycopg2.connect(dbname='mega_app', user='4bic',password='postgres', host='localhost', port='5432')
    # create a cursor object
    cur=conn.cursor()
    # add data
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    # commit to db
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(dbname='mega_app', user='4bic',password='postgres', host='localhost', port='5432')
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(dbname='mega_app', user='4bic',password='postgres', host='localhost', port='5432')
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect(dbname='mega_app', user='4bic',password='postgres', host='localhost', port='5432')
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

# create_table()
# insert("Mangoes", 50, 130)
# delete("Apple")
# update(86,75,'Oranges')
print (view())
