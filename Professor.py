class Professor:
    def __init__(self,nome, cpf, idTurma,idUsuario):
        self.nome = nome
        self.cpf = cpf
        self.idTurma = idTurma #referenciar o idTurma como chave estrangeira
        self.idUsuario = idUsuario #referenciar o idUsuario como chave estrangeira