from flask import Flask, render_template
import models

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/users")
def users():
    manageu = models.ManageUser()
    ulist = manageu.getuserlist()
    viewbag = []
    viewbag.append(len(ulist))
    viewbag.extend(ulist)
    return render_template('users.html', userlist = viewbag)

@app.route("/viewuser")
def viewuser(uid):
    manageu = models.ManageUser()
    user = manageu.getuserdetails(uid)
    viewbag = user
    return render_template('viewuser.html', user = viewbag)

if(__name__=="__main__"):
    models.Schema()
    app.run(debug=True)
