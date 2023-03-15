from flask import *
import sqlite3

app=Flask(__name__)

def dbcon():
    return  sqlite3.connect('./database.db')

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

@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route('/')
def index():
    stores=select_all()
    # print(stores)
    return render_template('index.html',stores=stores)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)