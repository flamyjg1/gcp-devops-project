from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<div style=\"text-align: center;\"><h1>Hello Everyone, I am Flamy!</h1><p>Welcome to GCP DevOps PROJECT 1.</p><p></p></div>'
