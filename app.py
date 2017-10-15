from __future__ import print_function
from future.standard_library import install_aliases

install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import urllib

import json, os, requests, sys, uuid, hashlib

from datetime import datetime
from flask import Flask, request, make_response, render_template, send_from_directory, redirect
from flask_debugtoolbar import DebugToolbarExtension
from process_request import process_request

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	return render_template('input.html')

@app.route('/urlpost', methods=["POST"])
def urlinput():
	uri = request.form.get('url')
	return process_request(uri)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)