class Turma:
    def __init__(self, id: int, horario: int, nivel, professor):
        # id da turma ai precisa ser id primaria/unica por turma, criar de formar automatica, fica no ar como faz isso.
        self.id = id
        self.horario = horario
        self.nivel = nivel
        self.professor = professor
        # referenciar um chave secundaria de nivel e professor (precisa criar as classes professor e nivel primeiro). criar dps.

   # def definir_horario(self):
    # O horario da turma deve ser definido com base no nivel da turma. Sendo assim, façamos
    def mostrarId(self):
        print(f'{self.id}')

turma1 = Turma(40028922, 22, "Branco", "Mikes")
turma1.mostrarId()
