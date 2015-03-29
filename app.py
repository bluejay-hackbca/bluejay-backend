# -*- coding: utf-8 -*-

import flask
from flask import Flask, request
from analyze import analyze
from convert import to_markdown



app = Flask(__name__)

@app.route("/submit", methods=['POST'])
def to_markdown():
    if request.method == "POST":
        # text = request.forms['text']
        text_fixture = "World War II (WWII or WW2), also known as the Second World War (after the recent Great War), was a global war that lasted from 1939 to 1945, though related conflicts began earlier. It involved the vast majority of the world's nations—including all of the great powers—eventually forming two opposing military alliances: the Allies and the Axis."
        text = text_fixture

        key_words = analyze(text_fixture);
        print(key_words)

        return "hurr"


if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=5000)
