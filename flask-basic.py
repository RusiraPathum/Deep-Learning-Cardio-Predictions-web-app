from flask import Flask, render_template

app = Flask(__name__) #flask object

@app.route('/')
def index():
    return "Welcome to the website"

@app.route('/page')
def page():
    return render_template(index.html)


app.run(debug=True)