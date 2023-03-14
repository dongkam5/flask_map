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

@app.route('/')
def index():
    return render_template('index.html')

def sol():
    return '''
    <div class="wrap">  
    <div class="info"> 
    <div class="title"> 카카오 스페이스닷원  <div class="close" onclick="closeOverlay()" title="닫기"></div></div>
<div class="body"> <div class="img"> <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
</div><div class="desc"><div class="ellipsis">제주특별자치도 제주시 첨단로 242</div> <div class="jibun ellipsis">(우) 63309 (지번) 영평동 2181</div>' + 
<div><a href="https://www.kakaocorp.com/main" target="_blank" class="link">홈페이지</a></div> </div> 
</div></div></div>'''

if __name__=='__main__':
    app.run(debug=True)