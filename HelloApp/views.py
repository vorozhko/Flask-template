from flask import Flask
from flask import render_template
from HelloApp import app

@app.route('/')
def home():
    return render_template("home.html", title = "Home")

# New functions
@app.route('/about')
def about():
        return render_template("about.html", title = "About us")

@app.route('/contact')
def contact():
        return render_template("contact.html", title = "Contact us")

@app.route('/hello/<name>')
def hello_there(name):
    from datetime import datetime
    now = datetime.now()
    date_formatted = now.strftime("%A, %d %B, %Y at %X")
    message = "Hello there, " + name + "!"

    return render_template(
        "hello_there.html",
        title ='Hello, Flask',
        message = message,
        date_formatted = date_formatted
    )

@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')