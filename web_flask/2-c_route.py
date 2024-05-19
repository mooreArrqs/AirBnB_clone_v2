#!/usr/bin/python3


""" Creating flask application """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False
""" Defining routes """


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!'.

    """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB'.

    """

    return'HBNB'


@app.route('/c/<text>')
def c_with_params(text):
    """
    Displays 'C' followed by the value of <text>.

    """

    text_no_underscore = text.replace('_', ' ')
    return 'C {}'.format(text_no_underscore)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
