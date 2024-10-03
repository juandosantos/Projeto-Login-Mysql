from flask import render_template, Blueprint

home_page = Blueprint("home", __name__)

@home_page.route("/")
def home():
    return render_template("index.html")