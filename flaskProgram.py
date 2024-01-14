from flask import Flask

app = Flask(__name__)

# create empty dictionary
users_dict={
}

@app.route('/addUsers')
def addUsers():
    users_dict={
    "name":"Kiran"
    }
    return users_dict


@app.route('/')
def getUsers():
    return users_dict

if __name__ == '__main__':
    app.run(debug=True)

