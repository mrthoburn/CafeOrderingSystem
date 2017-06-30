from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("index.html")

@app.route("/cart")
def cart():
    order = [("Pizza","Exra Cheese",7),("Coke","Not the Beverage",2),("Cookie","extra cookie",1)]
    price = 0
    for tup in order:
        price += tup[2]
    return render_template("cart.html",order=order,total=price)

@app.route("/submit")
def submit():
    return render_template("submit.html")
if __name__ == "__main__":
    app.run()

