# import add
# Importing flask.
from flask import Flask, request, jsonify

products = [{"name": "Coke",
             "price": 20},
            {"name": "pepsi",
            "price": 30}]
# Create the server
app = Flask(__name__)

# Root


@app.route("/")
def hello():
    print(" I am in hello function")
    return "<H1>Hello World</H1>"


@app.route("/api", methods=['GET', 'POST'])
def api():
    if (request.method == 'GET'):
        return (" You are getting a get request")
    elif (request.method == 'POST'):
        return jsonify("Post Request")


@app.route("/products", methods=['GET', 'POST'])
def product():
    if (request.method == 'GET'):
        return (products)
    elif (request.method == 'POST'):

        jsonData = request.get_json()
        print(request.get_json())
        products.append(jsonData)
        return jsonify("new product is added")


if (__name__ == "__main__"):
    app.run(debug=True)

