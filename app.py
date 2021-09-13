from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_from_xila():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
