from flask import Flask, render_template

server = Flask(__name__, static_folder = "static" )

@server.route("/")
def index():
    return render_template("index.html")

server.run (host = "0.0.0.0", port = 8080)


