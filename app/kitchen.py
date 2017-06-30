from flask import Flask, render_template, request
from flask_mail import Mail, Message
import random

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'upseats@gmail.com'
app.config['MAIL_PASSWORD'] = 'Noahsucks'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
theQueue = list()


@app.route("/main")
def main():
    global theQueue
    theQueue = initQueue()
    #print theQueue
    return render_template("queue.html", orders=theQueue)


@app.route("/makeOrder")
def makeOrder():
    order = getOrder()
    return render_template("kitchen.html", orders=order[0], comment=order[1], orderNum=order[2])


@app.route("/queue")
def queue():
    orderNum = request.args.get("orderNum")
    item = request.args.get("item")
    comment = request.args.get("comment")
    #print orderNum
    # Tell user that their order is ready
    thing = (int(orderNum), str(item), str(comment))
    print thing
    index = getQueueIndex(thing)
    print index
    recipient = theQueue[index][4]
    msg = Message('Hello', sender='upseats@gmail.com', recipients=[recipient])
    msg.body = "Your order is ready"
    # mail.send(msg)

    # Re-render the queue
    updateQueue(thing)
    return render_template("queue.html", orders=theQueue)


# Temporary method to make fake orders
def getOrder():
    orders = ["Pizza", "CheeseBurger", "Sandwich", "Deez nuts", "Deez nuts with Chipotle Sauce", "Just Chipotle Sauce",
              "Spagooter"]
    ingredients = ["apples, banannas", "chipotles, sauce", "the secret ingredient ;)"]
    comments = ["Nothing on it", "Extra chipotle sauce", "n/a"]
    recipients = ["usr1@ups.com", "usr2@ups.com", "usr3@ups.com"]
    return (random.choice(orders), random.choice(ingredients), random.choice(comments), random.randint(1000, 9999),
            random.choice(recipients))


def initQueue():
    with open("../order", "r") as file:
        temp = file.readlines()

    theQueue = [eval(x[:-1]) for x in temp]
    return theQueue


def updateQueue(orderNum):
    index = getQueueIndex(orderNum)

    for i in range(index, len(theQueue) - 1):
        global theQueue
        #print theQueue
        theQueue[i] = theQueue[i + 1]
    del theQueue[-1]


def getQueueIndex(order):
    j = 0
    #print theQueue
    for tup in theQueue:
        #print tup, order
        if tup[0] == order[0] and tup[1] == order[1] and tup[2] == order[2]:
            return j
        j += 1


if __name__ == "__main__":
    app.run(port=5001)
