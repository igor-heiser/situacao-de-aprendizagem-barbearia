# agendamentos.py
# Funções de acesso e manipulação dos dados da tabela agendamentos

import mysql.connector
from banco import conectar
from models import Agendamento


def listar_agendamentos():
    """
    Retorna uma lista de objetos Agendamento, ordenados por data e horário
    """
    conexao = None
    cursor = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, cliente, telefone, servico, preco, barbeiro, data, horario, status
            FROM agendamentos
            ORDER BY data, horario
        """)
        resultados = cursor.fetchall()
        for linha in resultados:
            lista.append(Agendamento.reverte_tupla(linha))
    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return lista


def buscar_agendamento(id):
    """
    Retorna um objeto Agendamento correspondente ao id informado,
    ou None caso não seja encontrado
    """
    conexao = None
    cursor = None
    agendamento = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, cliente, telefone, servico, preco, barbeiro, data, horario, status
            FROM agendamentos
            WHERE id = %s
        """, (id,))
        resultado = cursor.fetchone()
        if resultado is not None:
            agendamento = Agendamento.reverte_tupla(resultado)
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar agendamento: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return agendamento


def listar_por_status(status):
    """
    Retorna uma lista de objetos Agendamento filtrados por status
    """
    conexao = None
    cursor = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, cliente, telefone, servico, preco, barbeiro, data, horario, status
            FROM agendamentos
            WHERE status = %s
            ORDER BY data, horario
        """, (status,))
        resultados = cursor.fetchall()
        for linha in resultados:
            lista.append(Agendamento.reverte_tupla(linha))
    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos por status: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return lista