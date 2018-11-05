from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key ="secret"

#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') bootstrap form does this for me
FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LAST_NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
@app.route('/')
def index():

	return render_template("index.html")

@app.route('/process', methods=['post'])

def process():
	print("Got Post Info")
	if request.form['email'] == '' or request.form['first_name'] == '' or request.form['last_name'] == ''or request.form['password'] == '' or request.form['password_confirm'] == '':
		flash("*All fields are required")
	elif not FIRST_NAME_REGEX.match (request.form['first_name']):
		flash("*Name field cannot have numbers or special characters")
	elif not LAST_NAME_REGEX.match (request.form['last_name']):
		flash("*Name field cannot have numbers or special characters")
	elif len(request.form['password']) <8:
		flash("*Password must be greater than 8 characters long")
	elif request.form["password"] != request.form["password_confirm"]:
		flash("*Password confirmation doesn't match Password")
	
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)