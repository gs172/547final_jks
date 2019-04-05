"""
File name: final_server.py
Authors: Evan Jelly, Wesley Kendall, Ge Song
Assignment:  Image Processor Final Project
Due Date: 04/26/2019 23:59

Function: server
"""

import logging
from datetime import datetime
from flask import Flask, jsonify, request, render_template, url_for


app = Flask(__name__)


'''logging.basicConfig(filename='logfile_server.log', level=logging.INFO)
logging.info('---------------Server intiated---------------')'''


@app.errorhandler(400)
def bad_request(error=None):
    """ Error Handler - 400 - Bad Request. This function is called when
    when a request can not be fulfilled due to inproper syntax. The function
    return a JSON message with an HTML status code and message and updated
    status code.

    Returns:
        JSON: Jsonify message with 400 status code
    """
    message = {
            'status': 400,
            'message': 'malformed syntax: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp


@app.errorhandler(404)
def not_found(error=None):
    """ Error Handler - 404 - Not Found. This function is called when
    when a request can not be fulfilled due to the server not finding anything
    matching the Request-URL.

    Returns:
        JSON: Jsonify message with 400 status code
    """
    message = {
            'status': 404,
            'message': 'Error Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route("/", methods=["GET"])
def index():
    """ This address is used to check that the hrss_server is On.

    Returns:
        String
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
