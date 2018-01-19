# Janani Kalyanam
# creating my first view
# January 18, 2018


from flask import render_template
from flaskexample import app
from flask import request
import os, sys
sys.path.append('/Users/jananikalyanam/Documents/insight_application/PROJECT/scripts')
import model_scripts
import text_processing
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
    text = request.form['text']
    fout = open('/Users/jananikalyanam/Documents/insight_application/PROJECT/scripts/website.txt','w');
    output = model_scripts.get_relevant_hashtags('i love awards i think they are awesome go golden globes');
    fout.write(text);
    fout.close();
    processed_text = text.upper()
    return ' '.join(output)
