#!/usr/bin/python3
"""
Route:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C” followed by
the value of the text variable
(replace underscore _ symbols with a space)
/python/<text>: display “C” followed by
the value of the text variable
(replace underscore _ symbols with a space)
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bnb():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """returns text"""
    x = text.replace('_', ' ')
    return "C {}".format(x)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """returns text"""
    x = text.replace('_', ' ')
    return "Python {}".format(x)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """returns a number if only it's an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """returns a number if only it's an integer."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """displays even or an odd integer."""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, text="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, text="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
