from flask import Flask, render_template, request
import firebase

states = firebase.estados()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', pagina='Home')

@app.route('/van')
def van():
    return render_template('van.html', pagina='Faço Transporte', estados=states)

@app.route('/passa')
def passa():
    return render_template('passa.html', pagina='Procuro Transporte')

@app.route('/cidade', methods=['POST',])
def cidade():
    try:
        estado = request.form['Estado']
        return render_template('van.html', pagina='Faço Transporte', estados=states, cidades=firebase.cidades(estado))
    except:
        return render_template('van.html', pagina='Faço Transporte', estados=states)

app.run(debug=True)