from flask import Flask, request
from convert import TTM, MD_FIXTURE

app = Flask(__name__)


@app.route("/submit", methods=['POST'])
def to_markdown():
    if request.method=="POST":
        #text = request.form['text'];
        #print "printing:::"
        #print text

        # Manipulate the text here.
        #return TTM(text)
        return MD_FIXTURE




if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=5000)
