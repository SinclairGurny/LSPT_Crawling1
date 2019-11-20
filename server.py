from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/", methods = ["POST"] )
def receive_links():
    """
    py:function:: receive_links( post )
    :param post: POST request
    :returns Success status code: but sends POST to LA and DDS
    """

def send_outlinks( olinks ):
    """
    py:function:: send_outlinks( olinks )
    :param olinks: outlinks to send to LA
    :type olinks: dict
    :returns None: but sends POST to LA
    """
    return

def send_documents( docs ):
    """
    py:function:: send_documents( docs )
    :param docs: documents to send to DDS
    :type docs: list
    :returns None: but sends POST to DDS
    """
    return
