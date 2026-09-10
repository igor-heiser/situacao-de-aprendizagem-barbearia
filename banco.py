# banco.py
# Responsável por criar a conexão com o banco de dados MySQL

import mysql.connector
from config import DB_CONFIG


def conectar():
    """
    Cria e retorna uma conexão com o banco de dados MySQL,
    usando as credenciais definidas em config.py
    """
    conexao = mysql.connector.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    return conexao