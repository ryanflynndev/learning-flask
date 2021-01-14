from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/home')
def home():
    return "<h1>Home Page</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return f"<h1>This is a page for {name.upper()} </h1>"

if __name__ == '__main__':
    app.run(debug=True)