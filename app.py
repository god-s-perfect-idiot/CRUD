from flask import Flask
import models

app = Flask(__name__)

@app.route("/")
def hello():
    return "EH"

if(__name__=="__main__"):
    models.Schema()
    app.run(debug=True)
