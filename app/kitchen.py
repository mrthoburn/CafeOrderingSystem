from flask import Flask, render_template, request
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
theQueue = list()

@app.route("/main")
def main():
    initQueue()
    return render_template("queue.html", orders=theQueue)

@app.route("/makeOrder")
def makeOrder():
    order = getOrder()
    return render_template("kitchen.html",orders=order[0],comment=order[1],orderNum=order[2])

@app.route("/queue")
def queue():
    orderNum = request.args.get("orderNum")
    #Tell user that their order is ready
    msg = Message('Hello', sender='upseats@gmail.com', recipients=["mthoburn96@gmail.com"])
    msg.body = "This is a test"
    #mail.send(msg)

    #Re-render the queue
    updateQueue(orderNum)
    return render_template("queue.html", orders=theQueue)

#Temporary method to make fake orders
def getOrder():
    orders = ["Pizza","CheeseBurger","Sandwich","Deez nuts","Deez nuts with Chipotle Sauce","Just Chipotle Sauce","Spagooter"]

    comments =["Nothing on it", "Extra chipotle sauce", "n/a"]
    return (random.choice(orders),"Deez Nuts",random.choice(comments),random.randint(1000,9999))

def initQueue():
    for i in range(10):
        theQueue.append(getOrder())

def updateQueue(orderNum):
    index = 0
    j = 0

    for tup in theQueue:
        if tup[3] == int(orderNum):
            index = j
        j += 1
    print index, theQueue[index]

    for i in range(index,len(theQueue)-1):
        theQueue[i] = theQueue[i+1]
    theQueue[-1] = getOrder()
if __name__ == "__main__":
    app.run()