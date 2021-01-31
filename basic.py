from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/home')
def home():
    return "<h1>Home Page</h1>"

@app.route('/person/<name>')
def person(name):
    return f"<h1>This is a page for {name[100]} </h1>"

if __name__ == '__main__':
    app.run(debug=True)