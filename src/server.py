#!/usr/bin/python3

"""
Crawling Server
--
Receives requests from Link Analysis
Sends results back to Link Analysis
and Document Data Store

py:module:: server
:synopsis: RESTful API I/O for crawler
"""

import sys
import time
import threading
from http import HTTPStatus

import requests
from flask import Flask
from flask import request

from crawler import CrawlerProcess

app = Flask(__name__)

# Addresses of other servers
LA_URL = "http://localhost:8010" # testing address
#LA_URL = "http://lspt-link2.cs.rpi.edu:80" # real address
DDS_URL = "http://localhost:8020"

def run_job(links):
    """
    py:function:: run_job(links)
    Handle crawler and send results in a new thread
    :param links: input list from link analysis
    :type links: array of URLs (string)
    """
    print("INPUT LINKS: ", links)
    # Crawl cralwer logic on all_links
    print("--- Starting crawling ---")
    la_result, dds_result = CrawlerProcess(links)
    print("--- Finished crawling ---")
    # Send results back to Link Analysis
    global LA_URL
    send_post(LA_URL, la_result)
    # Send results to Document Data Store
    global DDS_URL
    send_put(DDS_URL, dds_result)


@app.route("/crawl", methods=["POST"])
def receive_links():
    """
    py:function:: receive_links()
    Handles POST request by Link Analysis
    :return OK: status code 200
    """
    all_links = request.json
    thread = threading.Thread(target=run_job, args=(all_links,))
    thread.start()
    return "OK", HTTPStatus.OK.value

def send_post(address, data):
    """
    py:function:: send_post(address, data)
    Sends POST request to address, containing data as json
    :param address: the server to send to
    :type address: string
    :param data: dictionary to include in POST request
    :type data: any
    """
    response = requests.post(address, json=data)
    if response.status_code != HTTPStatus.OK:
        sys.stderr.write("ERROR: while sending to "+address)

def send_put(address, data):
    """
    py:function:: send_put(address, data)
    Sends PUT request to address, containing data as json
    :param address
    :type address: string
    :param data: the data to send
    :type data: any
    """
    response = requests.put(address, json=data)
    if response.status_code != HTTPStatus.OK:
        sys.stderr.write("ERROR: while sending to "+address)

def test_crawler(links):
    """
    py:function:: test_crawler(links)
    Dummy function to simulate a crawler that finds nothing
    :param links: input list from link analysis
    :type links: list of URLs (string)
    :returns out_links, out_docs:
    :type out_links: dictionary input_link -> list of output_links
    :type out_dics: dictionary input_link -> document information
    """
    time.sleep(2) # simulate crawling sites
    out_links = {}
    out_docs = {}
    for tmp_link in links:
        out_links[tmp_link] = dict()
        out_docs[tmp_link] = dict()
    return out_links, out_docs


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=80)
