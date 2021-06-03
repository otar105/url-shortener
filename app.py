from flask import Flask, render_template, redirect, request, flash
import pyshorteners

app = Flask(__name__)
app.secret_key = "web"

@app.route("/")
def index_page():
    return render_template("index.html", have_link = True)

@app.route("/linksave", methods=["post"])
def linksave_page():
    shortener = pyshorteners.Shortener()
    link = request.form["link"]
    x = shortener.tinyurl.short(link)
    flash(f"Successfully created! link: {x}")
    return redirect("/")

if __name__ == "__main__":
    app.run()