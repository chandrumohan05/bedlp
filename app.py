from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to PythonAnywhere!"

@app.route('/hello')
def hello():
    return "Hello Students!"

if __name__ == '__main__':
    app.run(debug=True)