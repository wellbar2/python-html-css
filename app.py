from flask import Flask, url_for, request, session, g, redirect, abort, render_template
import sqlite3


DATABASE="blog.db"
SECRET_KEY='pudim'


app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def depois_requisicao(exc):
    g.bd.close()


@app.route('/')
@app.route('/entradas')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo':titulo, 'texto':texto})
    return render_template('exibir_entradas.html', entradas=entradas)

@app.route('/inserir')
def inserir_entrada():
    sql = 'INSERT INTO entradas(titulo,texto) VALUES ("Quarto post","Esse é o post 4")'
    g.bd.execute(sql)
    g.bd.commit()
    return redirect(url_for('exibir_entradas'))

@app.route('/hello')
def pagina_inicial():
    return "Olá Mundo"