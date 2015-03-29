from flask import Flask, request
from convert import TTM

app = Flask(__name__)

@app.route("/submit", methods=['POST'])
def to_markdown():
    if request.method=="POST":
        text = request.get("text");

        # Manipulate the text here.
        return TTM(text)



