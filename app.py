from flask import Flask, render_template,request
import models
import service

current_user = -1

app = Flask(__name__)

@app.route("/")
def home():
    global current_user
    current_user = -1
    return render_template('home.html')

@app.route("/users")
def users():
    viewbag = service.pullusers()
    return render_template('users.html', userlist = viewbag)

@app.route("/viewuser/<int:uid>",methods=['GET'])
def viewuser(uid):
    global current_user
    current_user = uid
    viewbag_user = service.pulluser(uid)
    viewbag_trans = service.pulltransactions(uid)
    message=""
    return render_template('viewuser.html', user = viewbag_user, transactions = viewbag_trans, message=message)

@app.route("/hub/<int:uid>",methods=['GET','POST'])
def hub(uid):
    global current_user
    if(current_user==uid):
        if request.method == 'POST':
            creds = request.form['amount']
            uid2 = request.form['recipient']
            user = current_user
            message = service.pushtransaction(user,uid2,creds)
            viewbag_user = service.pulluser(uid)
            viewbag_trans = service.pulltransactions(uid)
            return render_template('viewuser.html', user = viewbag_user, transactions = viewbag_trans, message = message)
        else:
            users = service.pullsenders(uid)
            sender = service.pulluser(uid)
            return render_template('hub.html', user=sender, ulist=users)
    else:
        return render_template('home.html')


if(__name__=="__main__"):
    models.Schema()
    app.run(debug=True)
