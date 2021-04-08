from qr import qrgen
from flask import  Flask,render_template, request, url_for, flash, redirect
from flask import *
import os
from db import get_customers, add_customers
# from shorter import get_short_url

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'
url_business = ''
url_short = ''
filename = ''
name = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converted',methods = ['GET'])
def convert():
    return render_template('converted.html')

@app.route('/download')
def download():
    print(url_business, name)
    qrgen(url_business, name)
    filename = '/tmp/' + name + '.png'
    return send_file(filename,as_attachment=True, cache_timeout=0), delete(filename)

def delete(filename):
    return os.remove(filename)

@app.route('/customers')
def customers():
    customers = get_customers()
    return render_template('customers.html', customers=customers)
#
# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        global name
        global url_business
        global url_short
        name = request.form['name']
        email = request.form['email']
        url_business = request.form['url_business']
        url_short = request.form.get("url_short", "0")

        # if url_short == "1":
        #     # url_business = get_short_url(url_business)
        if not name:
            print('Name is required!')
        elif not email:
            print('Email is required!')
        elif not url_business:
            print('Url is required!')
        else:
            #add_customers(name, email, url_business, url_short)
            return redirect(url_for('convert'))
    return render_template('create.html')


if __name__ == "__main__":
     app.run(debug=True)


