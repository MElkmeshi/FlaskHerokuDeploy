from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return "home"

if __name__ == "__main__":
    app.run()
