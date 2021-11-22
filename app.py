from flask import Flask
from flask import request
import os
import socket
import json
import nmap
from flask import json
from werkzeug.exceptions import HTTPException
from task import task

app = Flask(__name__)
tasks = task()


@app.route('/')
def index():
    return "this is index page"

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/gettasks', methods=['POST'])
def gettasks():
    result = dict()
    for key,value in tasks.tasklist.items():
        result[key] = value

    return json.dumps(result)


@app.route('/addtasks', methods=['POST'])
def addtasks():
    data = request.data
    data_j = json.loads(data)
    tasks.Add(data_j)
    return "success"


@app.route('/api/ip', methods=['POST'])
def getip():
    data = request.data
    data_j = json.loads(data)
    domain = data_j['domain']
    result_dict = {}

    for one_domain in domain:
        ip_list = list({addr[-1][0] for addr in socket.getaddrinfo(one_domain, 0, 0, 0, 0)})
        result_dict[one_domain] = ip_list
    
    result = json.dumps(result_dict)
    return result


if __name__ == '__main__':

    app.run()
