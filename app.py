from flask import Flask, render_template, jsonify, request
from stock_scraper import get_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/demo")
def demo():
	return render_template("demo.html")


@app.route("/data")
def data():
	return jsonify(get_data())

if __name__ == "__main__":
    app.run(debug=True)
