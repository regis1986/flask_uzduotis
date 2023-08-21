from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/orai")
def ora():
    return render_template('orai.html')

@app.route("/naujienos")
def naujienos():
    return render_template('naujienos.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('forma.html')
    if request.method == 'POST':
        vardas = request.form['laukelis']
        return render_template('vardas.html', sablono_kint=vardas)
    else:
        return render_template('forma.html')

@app.route('/<kintamasis>')
def user(kintamasis):
    return render_template('vardas.html', sablono_kint=kintamasis)

@app.route('/pasisveikink5', methods=['GET', 'POST'])
def pasisveikink5():
    if request.method == 'GET':
        return render_template('pasisveikink.html')
    if request.method == 'POST':
        vardas = request.form['laukelis']
        return render_template('pakartok.html', sablono_kint=vardas)
    else:
        return render_template('pasisveikink.html')

@app.route('/pakartok')
def pakartok():
    return render_template('pakartok.html')



if __name__ == "__main__":
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(host='0.0.0.0', port=port)