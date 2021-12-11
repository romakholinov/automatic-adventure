from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/cakesLine')
def cakesLine():
    return render_template("cakesLineGraph.html")
@app.route('/piesLine')
def piesLine():
    return render_template("piesLineGraph.html")
@app.route('/cookiesLine')
def cookiesLine():
    return render_template("cookiesLineGraph.html")
@app.route('/smoothiesLine')
def smoothiesLine():
    return render_template("smoothiesLineGraph.html")
@app.route('/coffeeLine')
def coffeeLine():
    return render_template("coffeeLineGraph.html")
@app.route('/cakesBar')
def cakesBar():
    return render_template("cakesBarGraph.html")
@app.route('/piesBar')
def piesBar():
    return render_template("piesBarGraph.html")
@app.route('/cookiesBar')
def cookiesBar():
    return render_template("cookiesBarGraph.html")
@app.route('/smoothiesBar')
def smoothiesBar():
    return render_template("smoothiesBarGraph.html")
@app.route('/coffeeBar')
def coffeeBar():
    return render_template("coffeeBarGraph.html")
@app.route('/foodComparison')
def foodComparison():
    return render_template("foodComparisonGraph.html")
@app.route('/drinksComparison')
def drinksComparison():
    return render_template("drinksComparisonGraph.html")
if __name__ == "__main__":
    app.run(debug=True)