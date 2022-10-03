import threading

from flask import Flask, render_template, request
import test_bot
from connectionSQL import ConnectionDatabase


app = Flask(__name__)


@app.route('/crear_cliente', methods=['GET', 'POST'])
def main():  # put application's code here
    personas = 0
    conn = ConnectionDatabase()
    conn.getConn()
    personas = conn.getLen()
    if request.method == 'POST' and request.form['nombre'] != "" and request.form['apellido'] != "" and request.form['telefono'] !=" " and request.form['direccion'] != "":
        conn.insert(request.form['nombre'], request.form['apellido'], request.form['telefono'], request.form['direccion'])
        conn.closeConn()
        return render_template('crear cliente.html', personas=personas+1)
    if request.method == 'GET':
        #aviso()
        conn.closeConn()
        return render_template('crear cliente.html', personas=personas)

@app.route('/chat_bot', methods=['GET', 'POST'])
def chat():  # put application's code here
    personas = 0
    conn = ConnectionDatabase()
    conn.getConn()
    personas = conn.getLen()
    if request.method == 'POST':
        try:
            insert_personas = int(request.form['personas'])
            if personas >= (insert_personas*-1):
                conn.insertDefault(request.form['personas'])
                personas = conn.getLen()
                conn.closeConn()
            return render_template('chat bot.html', personas=personas)
        except:
            return render_template('chat bot.html', personas=personas)
    if request.method == 'GET':
        conn.closeConn()
        return render_template('chat bot.html', personas=personas)

