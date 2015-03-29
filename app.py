# -*- coding: utf-8 -*-

import flask
from flask import Flask, request
from analyze import analyze
from convert import to_markdown



app = Flask(__name__)

@app.route("/submit", methods=['POST'])
def to_md():
    if request.method == "POST":
        text = request.form['text']
        #text_fixture = "World War II (WWII or WW2), also known as the Second World War (after the recent Great War), was a global war that lasted from 1939 to 1945, though related conflicts began earlier. It involved the vast majority of the world's nations—including all of the great powers—eventually forming two opposing military alliances: the Allies and the Axis."
        # text = text_fixture

        key_words = analyze(text);
        return to_markdown(text, key_words)


if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=5000)
