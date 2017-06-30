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
    recipient = theQueue[getQueueIndex(orderNum)][4]
    msg = Message('Hello', sender='upseats@gmail.com', recipients=[recipient])
    msg.body = "This is a test"
    #mail.send(msg)

    #Re-render the queue
    updateQueue(orderNum)
    return render_template("queue.html", orders=theQueue)

#Temporary method to make fake orders
def getOrder():
    orders = ["Pizza","CheeseBurger","Sandwich","Deez nuts","Deez nuts with Chipotle Sauce","Just Chipotle Sauce","Spagooter"]
    ingredients = ["apples, banannas", "chipotles, sauce", "the secret ingredient ;)"]
    comments =["Nothing on it", "Extra chipotle sauce", "n/a"]
    recipients = ["usr1@ups.com","usr2@ups.com","usr3@ups.com"]
    return (random.choice(orders),random.choice(ingredients),random.choice(comments),random.randint(1000,9999),random.choice(recipients))

def initQueue():
    for i in range(10):
        theQueue.append(getOrder())

def updateQueue(orderNum):
    index = getQueueIndex(orderNum)

    for i in range(index,len(theQueue)-1):
        theQueue[i] = theQueue[i+1]
    theQueue[-1] = getOrder()

def getQueueIndex(orderNum):
    j = 0
    for tup in theQueue:
        if tup[3] == int(orderNum):
            return j
        j += 1
if __name__ == "__main__":
    app.run()