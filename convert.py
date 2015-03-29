import wikipedia
gw = wikipedia.page("george washington")
gwImage = gw.images[0]
gwSummary = wikipedia.summary("george washington", sentences = 2)
print gwImage
print gwSummary
