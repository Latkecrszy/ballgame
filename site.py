from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("site.html")


app.run(host='0.0.0.0', port=80)
