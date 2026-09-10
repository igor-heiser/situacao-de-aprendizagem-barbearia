# 💈 Barbearia Navalha de Ouro

> **Sistema Web de Agendamentos** desenvolvido para a Situação de Aprendizagem da unidade curricular **Programação de Aplicativos**, do **Curso Técnico em Desenvolvimento de Sistemas — SENAI**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge" alt="Jinja2">
</p>

---

## 📌 Sobre o projeto

A **Barbearia Navalha de Ouro** controlava seus agendamentos em um caderno no balcão, o que causava horários duplicados e dificuldade para localizar clientes e acompanhar os atendimentos.

Este projeto substitui esse controle manual por um **sistema web** que permite listar, filtrar por status e consultar o detalhe de cada agendamento.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Linguagem principal |
| 🌐 Flask | Framework web e rotas |
| 🗄️ MySQL | Banco de dados |
| 🔌 mysql-connector-python | Conexão Python ↔ MySQL |
| 🧩 Jinja2 | Templates HTML dinâmicos |
| 🚀 Gunicorn | Execução em produção (deploy) |

---

## 📁 Estrutura do projeto

```text
barbearia/
├── app.py                # Aplicação Flask e rotas
├── agendamentos.py       # Consultas à tabela agendamentos
├── banco.py              # Conexão com o MySQL
├── config.py             # Credenciais de conexão
├── models.py             # Classe Agendamento (POO)
├── banco.sql             # Criação do banco + dados iniciais
├── requirements.txt      # Dependências
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── agendamentos.html
    └── detalhe.html
```

---

## 🌐 Rotas disponíveis

| Rota | Função |
|---|---|
| `/` | Início — nome da barbearia e total de agendamentos |
| `/agendamentos` | Lista todos os agendamentos |
| `/agendamentos/status/<status>` | Filtra por status (Agendado, Concluído, Cancelado) |
| `/agendamento/<id>` | Detalhe de um agendamento |

---

## 🚀 Como executar o projeto

### ▶ Acesso via deploy (Render)
O projeto está publicado no Render e pode ser acessado direto pelo link abaixo, sem instalação:

🔗 **[inserir link do deploy no Render]**

### ▶ Executando localmente

```bash
# 1. Entrar na pasta do projeto
cd barbearia

# 2. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Executar a aplicação
python app.py
```

Depois, acesse: `http://127.0.0.1:5000`

> ⚠️ Antes de rodar, crie o banco `barbearia` no MySQL Workbench, execute o `banco.sql` e ajuste as credenciais em `config.py` para o seu ambiente.

---

## 👥 Integrantes

- Igor Negherbon Heiser
- Arthur Pagliarini Martins
- Enzo Busarello

---

<p align="center">
  <strong>💈 Barbearia Navalha de Ouro</strong><br>
  Projeto acadêmico • SENAI • Programação de Aplicativos
</p>
