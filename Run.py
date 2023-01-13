from flask import Flask,render_template,request
from Admin_page import *
from login_page import *
from User_page import *


app = Flask(__name__)
app.secret_key = "Administrator"
app.register_blueprint(Document_products)
app.register_blueprint(User)
app.register_blueprint(Pageuse)

@app.route("/")
def index():
    if "username" not in session:
        return render_template("login/login.html")


@app.route("/indexAdmin")
def indexAdmin():
    if "username" not in session:
        return render_template("login/login.html")
    else:
        return redirect(url_for('Document_products.Admin_index'))

@app.route("/indexUser")
def indexUser():
    if "username" not in session:
        return render_template("login/login.html")
    else:
        return redirect(url_for('Pageuse.userindex'))

@app.route("/requisition")
def requisition():
    if "username" not in session:
        return render_template("login/login.html")
    else:
        return render_template("user/requisition.html")

@app.route("/petition")
def petition():
    if "username" not in session:
        return render_template("login/login.html")
    else:
        return render_template("admin/petition.html")

@app.route("/Borrow")
def Borrow():
    if "username" not in session:
        return render_template("login/login.html")
    else:
        return render_template("admin/Borrow.html")

if __name__ == "__main__":
    app.run(debug=True)
