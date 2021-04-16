# app.py
from flask import Flask           # import flask
from flask import jsonify
app = Flask(__name__)             # create an app instance
app.config["DEBUG"] = True

#Create some test data for our catalogue in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
] 

@app.route("/<name>", methods=['GET'])                   # at the end point /
def hello_name(name):                   # call method hello_name
    return "Hello "+name         # which returns "hello world"

# A route to return  all the available entried in the catalog.
@app.route("/api/v1/resources/books/all", methods=['GET'])
def api_all():
    return jsonify(books)

app.run()

