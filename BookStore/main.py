from flask import Flask, app, render_template

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('index.html')

app.run(debug=True)