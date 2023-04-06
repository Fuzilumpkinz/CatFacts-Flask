from flask import Flask, render_template, Response, request, redirect, url_for
import requests

app = Flask(__name__)
fact = ""



@app.route('/')
def index():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)
    fact = response.json()["fact"]
    return render_template('index.html', fact=fact)

@app.route("/catFact/", methods=['POST'])
def catFact():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)
    fact = response.json()["fact"]
    return render_template('index.html', fact=fact)


    