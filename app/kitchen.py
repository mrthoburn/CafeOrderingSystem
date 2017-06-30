from flask import Flask, render_template
from flask_mail import Mail, Message
import random

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
    orders = list()
    for i in range(10):
        orders.append(getOrder())
    return render_template("queue.html", orders=orders)

@app.route("/makeOrder", methods = ["POST"])
def makeOrder():
    order = getOrder()
    return render_template("kitchen.html",orders=order[0],comment=order[1],orderNum=order[2])

@app.route("/queue")
def queue():
    #Tell user that their order is ready
    msg = Message('Hello', sender='upseats@gmail.com', recipients=["mthoburn96@gmail.com"])
    msg.body = "This is a test"
    #mail.send(msg)

    #Re-render the queue
    orders = list()
    for i in range(10):
        orders.append(getOrder())
    return render_template("queue.html", orders=orders)

#Temporary method to make fake orders
def getOrder():
    orders = ["Pizza","CheeseBurger","Sandwich","Fresh Dick","Fresh Dick with Chipotle Sauce","Just Chipotle Sauce","Pour chipotle sauce over my naked body"]
    comments =["Nothing on it", "Extra chipotle sauce", "its been a rough day, sneak some whiskey in for me"]
    return (random.choice(orders), random.choice(comments),random.randint(1000,9999))

if __name__ == "__main__":
    app.run()