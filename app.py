import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/details")
def project_details():
    """Endpoint to display project details."""
    details = {
        "project": "Flask Sample App",
        "version": "1.0",
        "description": "This is a sample Flask application."
    }
    return f"Hello World! Here are the project details: {details}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
