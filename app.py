from flask import Flask,render_template,url_for,request,redirect,flash,session
from flask_mysqldb import MySQL
import yaml
from datetime import date
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
import pandas as pd
import csv

app=Flask(__name__)
app.secret_key = "mykey"


#configure db
db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']

mysql=MySQL(app)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        f = request.files['csvfile']
        f.save(secure_filename(f.filename))
        return redirect(url_for('home'))
    else:
        return render_template('index.html')



if __name__ =='__main__':
    app.run(debug=True,threaded = True )