# Using flask for simple webhook initialization in order to run our webpage.
# Not necessary to use django as much of what django can do, flask can do in a more lightweight way
from flask import Flask, redirect, url_for, render_template, request, jsonify
from static.Backend.algorithm import coinToss
from flask_cors import CORS, cross_origin
import os
import json

# Declaring the app
app = Flask(__name__)
cors = CORS(app)


# Render homepage
@app.route("/")
def main():
    return render_template('index.html')


# Route for CoinToss
@app.route("/test", methods=['GET', "POST"])
def test():
    if request.method == "GET":
        data = {"picked": "1"}
        j = json.dumps(data)
        print("######################")
        return jsonify(j)

    if request.method == "POST":
        incomDATA = request.data
        s = int(''.join(filter(str.isdigit, str(incomDATA))))
        v = coinToss(s)
        return jsonify(v)


# Route for CoinToss
@ app.route("/flipCoin", methods=['POST'])
def flipCoin():
    v = request.args.get('data')
    print(v)
    return coinToss(v)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
