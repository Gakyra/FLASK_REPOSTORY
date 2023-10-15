import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv(


)
app = Flask(__name__)


@app.route("/main")
def main_func():
    return "This is a main package!"


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))