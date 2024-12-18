from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return 'Hello, World!' at the root URL"""

    return 'Hello, World!'