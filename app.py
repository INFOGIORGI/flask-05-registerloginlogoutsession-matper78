from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=='GET':
        return render_template("register.html")
    else:
        pass
        nome= request.form.get("nome")
        return redirect(url_for('welcome'))


@app.route("/login")
def login():
    return render_template("login.html")


app.run(debug=True)
