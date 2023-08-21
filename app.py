from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/orai")
def ora():
    return render_template('orai.html')

if __name__ == "__main__":
    app.run()