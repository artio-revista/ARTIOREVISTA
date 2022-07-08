from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre-nos')
def sobre_nos():
    return render_template('about-us.html')

@app.route('/revista')
def revista_home():
  return render_template('home.html')

@app.route('/revista/<id>')
def revista(id):

  if id == '1' :
    return render_template('revista1.html')

  else:
    return render_template('home.html')

@app.route('/catalogo')
def catalogo():
  edicoes = [
    {1, "https://artio-or-flask.wendelkaue.repl.co/revista/1"},
    {2, "https://artio-or-flask.wendelkaue.repl.co/revista/2"},
    {3, "https://artio-or-flask.wendelkaue.repl.co/revista/3"}
  ]

  return render_template('catalogo.html', edicoes=edicoes)

app.run(host='0.0.0.0', port=81)