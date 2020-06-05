from flask import Flask, render_template
import models
import service

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/users")
def users():
    viewbag = service.pullusers()
    return render_template('users.html', userlist = viewbag)

@app.route("/viewuser/<int:uid>",methods=['GET'])
def viewuser(uid):
    viewbag_user = service.pulluser(uid)
    viewbag_trans = service.pulltransactions(uid)
    return render_template('viewuser.html', user = viewbag_user, transactions = viewbag_trans)

@app.route("/transferhub/<int:uid1>",methods=['GET'])
def transferhub(uid1):
    users = service.pullusers()
    sender = service.pulluser(uid1)
    return render_template('transferhub', user=sender, ulist=users)

@app.route("/send/<int:uid1><int:uid2><int:creds>",methods=['GET'])
def send(uid1,uid2,creds):
    service.pushtransaction(uid1,uid2,creds)
    users = service.pullusers()
    sender = service.pulluser(uid)
    return render_template('send', user=sender, ulist=users)

if(__name__=="__main__"):
    models.Schema()
    app.run(debug=True)
