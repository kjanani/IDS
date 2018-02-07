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

@app.route('/')
def my_form():
    return render_template('input.html',tweet_text='')

@app.route('/', methods=['POST'])
def my_form_post():
    tweet = request.form['tweet']
    tweet_text = tweet;
    hashtags = model_scripts.get_relevant_hashtags(tweet);
    print(tweet)
    return render_template('input.html',hashtags = hashtags,tweet_text=tweet_text)
