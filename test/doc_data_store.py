"""
Dummy Document Data Store Server
--
"""

from flask import Flask
from flask import request

APP = Flask(__name__)

@APP.route("/", methods = ["PUT"] )
def add_documents():
    """
    py:function:: add_documents()
    :param put: PUT request
    :returns Success status code:
    """
    # Print out documents
    print(request.json)
    return "OK", 200
