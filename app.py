from flask import Flask, request, session, g, redirect, abort, render_template
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
def exibir_entradas():
    return "<h1>Aqui estarão as postagens</h1>"

@app.route('/hello')
def pagina_inicial():
    return "Olá Mundo"