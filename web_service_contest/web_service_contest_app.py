from flask import Flask, Response, request
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello"


@app.route('/register')
def register_user():
    
    name = request.args.get("name")
    host = request.args.get("host")
    port = request.args.get("port")

    for param in [host, port, name]:
        if not param:
            return Response('Не хватает обязательного параметра {}'.format(param), 404)

    with open('services.json', 'a') as fin:
        service_info = {'host': host, 'name': name, 'port': int(port)}
        json.dump(service_info, fin)
        fin.write('\n')
    
    return 'Регистрация прошла успешно'
