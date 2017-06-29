from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signIn')
def signUp():
    name = request.form['inputName']


if __name__ == "__main__":
    app.run()

