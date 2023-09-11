from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_map():
    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True)
