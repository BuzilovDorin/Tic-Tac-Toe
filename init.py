# Using flask for simple webhook initialization in order to run our webpage.
# Not necessary to use django as much of what django can do, flask can do in a more lightweight way
from flask import Flask, redirect, url_for, render_template

# Declaring the app
app = Flask(__name__)


# Initialize and app route which is "/"
@app.route("/")
# render the html page
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
