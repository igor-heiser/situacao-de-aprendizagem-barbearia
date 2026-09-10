# models.py
# Define a classe Agendamento, representando um registro da tabela agendamentos

class Agendamento:
    def __init__(self, cliente, telefone, servico, preco, barbeiro, data, horario, status="Agendado", id=None):
        self.id = id
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

    def exibir(self):
        """
        Retorna os dados do agendamento formatados em uma única linha
        """
        return (f"[{self.id}] {self.cliente} - {self.servico} com {self.barbeiro} "
                f"em {self.data} às {self.horario} | R$ {self.preco} | Status: {self.status}")

    def converte_tupla(self):
        """
        Converte o objeto Agendamento em uma tupla,
        útil para inserção/atualização no banco de dados
        """
        return (self.cliente, self.telefone, self.servico, self.preco,
                self.barbeiro, self.data, self.horario, self.status)

    @staticmethod
    def reverte_tupla(tupla):
        """
        Recebe uma tupla vinda do banco de dados (linha da tabela)
        e retorna um objeto Agendamento correspondente.
        Ordem esperada da tupla:
        (id, cliente, telefone, servico, preco, barbeiro, data, horario, status)
        """
        return Agendamento(
            id=tupla[0],
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=tupla[4],
            barbeiro=tupla[5],
            data=tupla[6],
            horario=tupla[7],
            status=tupla[8]
        )