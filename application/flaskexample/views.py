# Janani Kalyanam
# creating my first view
# January 18, 2018


from flask import render_template
from flaskexample import app
import requests
#@app.route('/')
#@app.route('/index')
#def index():
#    user = { 'nickname': 'Miguel' } # fake user
#    return render_template("index.html", title = 'Home', user = user)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    ext = request.form['text']
    processed_text = text.upper()
    return processed_text
