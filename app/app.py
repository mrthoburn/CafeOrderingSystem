from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("index.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/submit")
def submit():
    return render_template("submit.html")
if __name__ == "__main__":
    app.run()

