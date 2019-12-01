"""
Dummy Document Data Store Server
--
"""

from flask import Flask

APP = Flask(__name__)

@APP.route("/", methods = ["PUT"] )
def add_documents():
    """
    py:function:: add_documents()
    :param put: PUT request
    :returns Success status code:
    """
    # Print out documents    
    
    return 200
