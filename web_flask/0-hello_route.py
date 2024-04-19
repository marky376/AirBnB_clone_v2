from flask import Flask

app = FLASK(__name__)

@app.route('/')
def hello():
    return 'Hello HBNB!'

