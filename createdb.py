import pandas as pd
import sqlite3

def dbcon():
    return  sqlite3.connect('./database.db')

def create_table():
    try:
        db=dbcon()
        cur=db.cursor()
        cur.execute("CREATE TABLE STORES (name varchar(50), address varchar(100), lat DOUBLE(10),lng DOUBLE(10),criteria varchar(20))")
        db.commit()
    except Exception as e:
        print('db error: ',e)
    finally:
        db.close()

def insert_data(item_list):
    db=dbcon()
    try:
        cur= db.cursor()
        for item in item_list:
            setdata=item
            cur.execute("INSERT INTO STORES VALUES (?,?,?,?,?)",setdata)
            db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
def delete_table():
    try:
        db=dbcon()
        cur=db.cursor()
        cur.execute("DROP TABLE STORES;")
        db.commit()
    except Exception as e:
        print('db error: ',e)
    finally:
        db.close()

def check_table():
    try:
        db=dbcon()
        cur=db.cursor()
        cur.execute('SELECT COUNT (*) FROM sqlite_master where name= "STORES"')
        result=cur.fetchone()
        return result
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db=dbcon()
        cur=db.cursor()
        cur.execute("SELECT * FROM STORES")
        ret=cur.fetchall()
    except Exception as e:
        print('db Error:',e)
    finally:
        db.close()
        return ret

df = pd.read_csv('data.csv', index_col='순번')
item=df.dropna()
item_list=item.values.tolist()
stores=[]
for item in item_list:
    if "화명" in item[1]:
        stores.append(item)
if not(check_table()):
    delete_table()
    create_table()
    insert_data(stores)
else:
    delete_table()
    create_table()
    insert_data(stores)

all_val=select_all()

for val in all_val:
    print(val)


