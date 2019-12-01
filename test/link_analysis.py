"""
Dummy Link Analysis Server
--
"""

from flask import Flask

APP = Flask(__name__)

URL_QUEUE = [] # total queue of URLs to process
REQ_SIZE = 4 # number of URLs to send per request


def read_url_file(filename):
    """
    py:function:: read_url_file()
    Read file containing links to test
    """
    print(filename)
    return True

@APP.route("/start", methods=["GET"])
def start():
    """
    py:function:: start()
    Start link analysis dummy server
    :param req: GET request
    :returns Succes status code
    """
    return 200

@APP.route("/", methods=["POST"])
def respond():
    """
    py:function::respond()
    responds to crawlers response with more links
    """
    return 200
