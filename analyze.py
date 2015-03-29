# -*- coding: utf-8 -*-


from __future__ import print_function
import semantria
import uuid
import time

serializer = semantria.JsonSerializer()

session = semantria.Session("dfbebbb5-af94-43b4-96e0-81894a9bc3d3", "e28ebdff-84ef-478d-82a2-5b1f07284eb8", serializer, use_compression=True)

def analyze(text):
    doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}
 
    status = session.queueDocument(doc)
    if status == 202:
        print("\"", doc["id"], "\" document queued successfully.", "\r\n")
    
    length = 1
    search_results = []
    results = {}

    while len(search_results) < length:
        print("Retrieving your processed results...", "\r\n")
        time.sleep(2)
    # get processed documents
        status = session.getProcessedDocuments()
        search_results.extend(status)

    for data in search_results:
        # print document sentiment score
        print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")
        results["document_id"] = str(data["id"])

        # print document themes
        if "themes" in data:
            themes = []
            print("Document themes:", "\r\n")
            for theme in data["themes"]:
                themes.append(str(theme["title"]))
                print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")
            print(themes)
            results["themes"] = themes

        # print document entities
        if "entities" in data:
            entities = []
            print("Entities:", "\r\n")
            for entity in data["entities"]:
                entities.append(str(entity['title']))
                print("\t", entity["title"], " : ", entity["entity_type"]," (sentiment: ", entity["sentiment_score"], ")", "\r\n")         
            results["entities"] = entities
    return results
