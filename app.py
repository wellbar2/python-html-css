from flask import Flask, request, session, g, redirect, abort, render_template
import sqlite3


DATABASE="blog.db"
SECRET_KEY='pudim'


app = Flask(__name__)

@app.route('/hello')

def pagina_inicial():
    return "Olá Mundo"