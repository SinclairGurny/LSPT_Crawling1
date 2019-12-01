"""
Crawling Server
--
Receives requests from Link Analysis
Sends results back to Link Analysis
and Document Data Store
"""


import json
from flask import Flask
from flask import request

APP = Flask(__name__)

@APP.route("/", methods=["POST"])
def receive_links():
    """
    py:function:: receive_links( post )
    :param post: POST request
    :returns Success status code: but sends POST to LA and DDS
    """
    return 200

def send_outlinks(olinks):
    """
    py:function:: send_outlinks( olinks )
    :param olinks: outlinks to send to LA
    :type olinks: dict
    :returns None: but sends POST to LA
    """
    print(olinks)

def send_documents(docs):
    """
    py:function:: send_documents( docs )
    :param docs: documents to send to DDS
    :type docs: list
    :returns None: but sends POST to DDS
    """
    print(docs)
