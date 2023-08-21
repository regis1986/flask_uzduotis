from flask import Flask, render_template, request

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

if __name__ == "__main__":
    app.run()