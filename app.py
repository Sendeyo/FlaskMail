from flask import Flask, render_template, request, url_for, redirect, session
import os
from passlib.hash import sha256_crypt
# import fun, data
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = os.urandom(24)


app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'anonymaxdashone@gmail.com',
	MAIL_PASSWORD = '17571757'
	)
mail = Mail(app)

buses = [""]

def send_mail(email, subject, message):
	try:
		msg = Message("My Test Emails!",
		  sender="anonymaxdashone@gmail.com",
		  recipients=[email])
		msg.body = message       
		mail.send(msg)
		return 'Mail sent!'
	except Exception as e:
		return(str(e)) 

@app.route("/emailSender", methods = ["GET", "POST"])
def EmailSender():
	if request.method == "POST":
		to = request.form["recipient"]
		subject = request.form["subject"]
		email = request.form["email"]
		# em = "{}  {}  {}".format(to, subject, email)
		send_mail(to, subject, email)
	return render_template("/editor.html")

@app.route("/")
def Home():
    return redirect("/emailSender")

if __name__ == "__main__":
	app.run(debug = True)