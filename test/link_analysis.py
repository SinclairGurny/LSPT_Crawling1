"""
Dummy Link Analysis Server
--
"""

import sys
import requests
from flask import Flask
from flask import request
from flask import jsonify

# === Global Variables ===

CRAWL_URL = "http://localhost:8000"

TEST_FILE = "test_urls1.txt"

URL_QUEUE = [] # total queue of URLs to process
REQ_SIZE = 4 # number of URLs to send per request

def read_url_file(filename):
    """
    py:function:: read_url_file()
    Read file containing links to test
    """
    try:
        global URL_QUEUE
        f = open(filename, "r")
        for url in f:
            URL_QUEUE.append(url)
    except:
        sys.stderr.write("ERROR: error while reading input file\n")
        sys.exit(1)

def setup():
    """
    """
    global TEST_FILE
    read_url_file(TEST_FILE)
    print("Dummy Link Analysis server ready")
    print("Starting test ...")
    send_next_request()

def send_next_request():
    """
    """
    global CRAWL_URL
    global URL_QUEUE
    global REQ_SIZE
    remaining_urls = len(URL_QUEUE)
    if remaining_urls == 0:
        return
    print(remaining_urls, " remaining URLS")
    last = min(REQ_SIZE, remaining_urls)
    req_list = URL_QUEUE[:last]
    URL_QUEUE = URL_QUEUE[last:]
    data = {"links": req_list}
    response = requests.post(CRAWL_URL, json=data)

# === Setup ===
def create_app():
    setup()
    return Flask(__name__)

APP = create_app()
    
# === Flask functions ===
    
@APP.route("/", methods=["POST"])
def respond():
    """
    py:function::respond()
    responds to crawlers response with more links
    """
    # Print response
    print(request.json)
    # Send next set
    send_next_request()
    return "OK", 200

if __name__ == "__main__":
    setup()
