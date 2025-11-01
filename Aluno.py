from Turma import Turma

class Aluno:
    def __init__(self, nome:str| None, idade: int| None, matricula: int | None, idTurma, idInscricaoExame: int | None, usuarioId: int | None) :
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.turma = Turma(self.turma.id) #referenciar o idTurma como chave estrangeira
        self.idInscricaoExame = idInscricaoExame #referenciar o idInscricaoExame como chave estrangeira
        self.usuarioId = usuarioId #referenciar o usuarioId como chave estrangeira

    def registrarAluno(self, nome, idade, matricula, usuarioid, idturma, id_inscricao_exame):
        self.nome = nome
        self.idade = idade

    #def mostrarDadosAluno(self):
        #print(Turma.mostrarId(self.id))

#aluno1 = Aluno("Mike", 21, None, Turma(id), 0, None,)
#aluno1.mostrarDadosAluno()

