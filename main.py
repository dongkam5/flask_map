from flask import *
import sqlite3

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)