# Import dependencies
from flask import Flask

# Create a new Flask app Instance
app = Flask(__name__)

# Create Flask routes
@app.route('/')
def hello_world():
    return "Hello world"
