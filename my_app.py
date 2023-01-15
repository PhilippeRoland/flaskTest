from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/my_app/<name>", methods=['GET', 'POST'])
def hello_world(name):
    return f'Hello {name}! You used {request.method} to get here'

@app.post("/post_only_method")
def post_only():
    return 'Special POST decorated method'

@app.route("/")
def index_routes():
    endpoints_it = map(lambda rule: f'{rule.endpoint} - {rule.methods}: {rule.rule}', app.url_map.iter_rules())
    return "</br>".join(list(endpoints_it))