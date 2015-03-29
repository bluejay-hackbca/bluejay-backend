# -*- coding: utf-8 -*-

import flask
from flask import Flask, request
import semantria
import time
import uuid

app = Flask(__name__)

@app.route("/submit", methods=['POST'])
def to_markdown():
    if request.method == "POST":
        serializer = semantria.JsonSerializer()
        session = semantria.Session("dfbebbb5-af94-43b4-96e0-81894a9bc3d3", "e28ebdff-84ef-478d-82a2-5b1f07284eb8", serializer, use_compression=True)

        text = request.form['text'];
        doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}
        status = session.queueDocument(doc)
        if status == 202:
            print("\"%s\" document queued successfully." % doc["id"])

        retrieved = False
        results = []

        while len(results) == 0:
            time.sleep(1)
            status = session.getProcessedDocuments()
            results.extend(status)

        data = results[0]
        document = {"Document: ", str(data["id"])}
        entities = []
        for entity in data["entities"]:
            entities.append(str(entity["title"]))

        return flask.jsonify({"words": entities})


if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=5000)
