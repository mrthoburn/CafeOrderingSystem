from flask import Flask, render_template
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'upseats@gmail.com'
app.config['MAIL_PASSWORD'] = 'Noahsucks'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/main")
def main():
    return render_template("kitchen.html")

@app.route("/done")
def done():
    msg = Message('Hello', sender='upseats@gmail.com', recipients=["mthoburn96@gmail.com"])
    msg.body = "This is a test"
    mail.send(msg)
    return render_template("kitchen.html")

if __name__ == "__main__":
    app.run()