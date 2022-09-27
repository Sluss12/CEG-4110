import csv
from genericpath import exists
from operator import index
import string
# Python basics
import sys, os, re, pprint
import random

from datetime import timedelta


# Flask app
from flask import Flask, make_response, render_template, render_template_string
from flask import jsonify, session, request, redirect, url_for
from markupsafe import escape

# --- APP SETUP ---

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    page = render_template('index.html')
    return page


# --- GLOBALS --- 

DEBUG = False

if __name__ == "__main__":

    DEBUG = True

    # Disable browser caching in dev to see changes on the fly
    # Only do this in debug mode, as slows down site
    @app.after_request
    def set_response_headers(response): 
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    if (len(sys.argv) > 1):
        with app.test_request_context():
            pass
         

    else:
        app.run(host="127.0.0.1",port=5000,debug=True)