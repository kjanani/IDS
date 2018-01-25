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
from wordcloud import WordCloud

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    tweet = request.form['tweet']
    output = model_scripts.get_relevant_hashtags(tweet);
    return render_template('input.html',hashtags = output)
