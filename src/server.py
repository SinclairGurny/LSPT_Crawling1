"""
Crawling Server
--
Receives requests from Link Analysis
Sends results back to Link Analysis
and Document Data Store
"""

import sys
import time
import requests
import threading
from http import HTTPStatus
from flask import Flask
from flask import request

APP = Flask(__name__)

LA_URL = "http://localhost:8010"
DDS_URL = "http://localhost:8020"

def run_job( links ):
    """
    """
    # Crawl cralwer logic on all_links
    la_result, dds_result = test_crawler(links)
    # Send results back to Link Analysis
    global LA_URL
    send_post(LA_URL, la_result)
    # Send results to Document Data Store
    global DDS_URL
    send_put(DDS_URL, dds_result)


@APP.route("/", methods=["POST"])
def receive_links():
    """
    py:function:: receive_links( post )
    :param post: POST request
    :returns Success status code: but sends POST to LA and DDS
    """
    all_links = request.json["links"]
    thread = threading.Thread(target=run_job, args=(all_links,))
    thread.start()
    return "OK", HTTPStatus.OK.value

def send_post(address, data):
    """
    py:function:: send_post(address, data)
    Sends POST request to address containing data in body
    :param address: the server to send to
    :param data: dictionary to include in POST request
    """
    response = requests.post(address, json=data)
    if response.status_code != HTTPStatus.OK:
        sys.stderr.write("ERROR: while sending to "+address)

def send_put(address, data):
    """
    """
    response = requests.put(address, json=data)
    if response.status_code != HTTPStatus.OK:
        sys.stderr.write("ERROR: while sending to "+address)

def test_crawler(links):
    """
    py:function:: test_crawler(links)
    Dummy function to simulate a crawler that found nothing
    """
    time.sleep(2)
    out_links = {}
    out_docs = {}
    for tmp_link in links:
        out_links[tmp_link] = dict()
        out_docs[tmp_link] = dict()
    return out_links, out_docs
