from flask import Flask, render_template
import firebase


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/van')
def van():
    return render_template('van.html')

@app.route('/passa')
def passa():
    return render_template('passa.html')


app.run(debug=True)