# app.py
# Aplicação Flask - Sistema de agendamentos da Barbearia Navalha de Ouro

from flask import Flask, render_template
from agendamentos import listar_agendamentos, buscar_agendamento, listar_por_status

app = Flask(__name__)

NOME_BARBEARIA = "Barbearia Navalha de Ouro"


@app.route('/')
def index():
    agendamentos = listar_agendamentos()
    return render_template('index.html', nome_barbearia=NOME_BARBEARIA, agendamentos=agendamentos)


@app.route('/agendamentos')
def agendamentos():
    lista = listar_agendamentos()
    return render_template('agendamentos.html', agendamentos=lista, nome_barbearia=NOME_BARBEARIA)


@app.route('/agendamentos/status/<status>')
def agendamentos_status(status):
    lista = listar_por_status(status)
    return render_template('agendamentos.html', agendamentos=lista, nome_barbearia=NOME_BARBEARIA)


@app.route('/agendamento/<int:id>')
def detalhe(id):
    agendamento = buscar_agendamento(id)
    return render_template('detalhe.html', agendamento=agendamento, nome_barbearia=NOME_BARBEARIA)


if __name__ == '__main__':
    app.run(debug=True)