from flask import Flask
from string import Template
import json

app = Flask(__name__)


DATABASE = 'services.json'


def get_services(filename):
    services = []
    with open(filename) as json_file:
        data = json.load(json_file)
        for service in data:
            services.append((service['name'], service['host'], service['port']))

    return services


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
        table_lines += table_line.substitute(name=service[0], host=service[1], port=service[2], status="GOOD", requests=10)
    return table_head + table_lines + table_end
