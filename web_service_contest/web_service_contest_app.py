from flask import Flask, Response
from string import Template
import json
import requests
from requests.exceptions import InvalidSchema

app = Flask(__name__)


DATABASE = 'services.json'


def get_services(filename):

    with open(filename) as json_file:
        data = json.load(json_file)

    return data


def check_service(host, port, name):
    url = '{host}:{port}/{name}'.format(host=host, port=port, name=name)

    try:
        response = requests.get(url=url)
    except InvalidSchema:
        return 'Not alive'

    if response.ok:
        return 'Alive'
    else:
        return 'Not alive'


@app.route('/')
def hello_world():
    table_head  = '''
    
    <style>
table, th, td {
  border: 1px solid black;
}
</style>
    
    <table style="width:100%">
  <tr>
    <th>Service</th>
    <th>Host</th> 
    <th>Port</th>
    <th>Status</th>
    <th>request nums</th>
  </tr>'''

    table_end = '''</table>'''

    table_line = Template('''
    <tr>
    <td><center>$name</center></td>
    <td><center>$host</center></td>
    <td><center>$port</center></td>
    <td>$status</td>
    <td>$requests</td>
  </tr>
  ''')

    #services = [('wiki','127.0.0.0.1','80',10)]
    services = get_services(DATABASE)
    table_lines = ''

    for service in services:
        host = service['host']
        port = service['port']
        name = service['name']

        service_status = check_service(host, port, name)
        table_lines += table_line.substitute(name=name, host=host, port=port, status=service_status, requests=0)
    return table_head + table_lines + table_end
