# app.py
from flask import Flask           # import flask
from catalogue import books
from flask import jsonify

app = Flask(__name__)             # create an app instance
app.config["DEBUG"] = True

@app.route("/<name>", methods=['GET'])                   # at the end point /
def hello_name(name):                   # call method hello_name
    return "Hello "+name         # which returns "hello world"

# A route to return  all the available entried in the catalog.
@app.route("/api/v1/resources/books/all", methods=['GET'])
def api_all():
    return jsonify(books)

app.run()

