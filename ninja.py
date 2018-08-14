from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("front.html")

@app.route('/ninja')
def ninja():
	return render_template("ninja.html")

@app.route('/ninja/blue')
def leonardo():
	return render_template("leonardo.html")

@app.route('/ninja/orange')
def michelangelo():
	return render_template("michelangelo.html")

@app.route('/ninja/red')
def raphael():
	return render_template("raphael.html")

@app.route('/ninja/purple')
def donatello():
	return render_template("donatello.html")

@app.route('/ninja/<el>')
def april(el):
	return render_template("notapril.html")

app.run(debug=True)	