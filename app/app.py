from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("index.html")

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signIn')
def signUp():
    name = request.form['inputName']
@app.route('/grocery')

# Example of passing content to html
def grocery():
    food = ["Beer", "Steak" , "Chicken" , "Tacos"]
    return render_template("grocery.html", food=food)


if __name__ == "__main__":
    app.run()

