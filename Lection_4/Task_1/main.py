from flask import Flask, render_template, request

server = Flask(__name__)

@server.route("/")
def index():
    
    return render_template("index.html")
    
@server.route("/plus")
def plus():

    value1= float(request.args.get("value1"))
    value2 = float(request.args.get("value2"))
    value= value1 + value2
    
    return render_template('result.html', value=value)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)