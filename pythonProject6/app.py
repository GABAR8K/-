from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def calculator():
    if request.method == 'POST':
        bebra = request.form['title']
        title = request.form['znak']
        popa = request.form['text']

        def getanswer(simwol, num1, num2):
            num1 = int(num1)
            num2 = int(num2)
            if simwol == "+":
                return str(num1 + num2)
            if simwol == "-":
                return str(num1 - num2)
            if simwol == "/":
                return str(num1 * num2)
            if simwol == "*":
                return str(num1 / num2)
            if simwol == "//":
                return str(num1 // num2)
            if simwol == "%":
                return str(num1 % num2)

        return render_template("genius.html", answer = getanswer(title, bebra, popa))
    else:
        return render_template("genius.html")



if __name__ == "__main__":
    app.run(debug=True)