 #   Programacao Orientada a Objetos (poo)

#Paradigma

#programacao funcional
#programacao logica
#programacao orientada a eventos
#programacao estruturada

# Programacao Orientada a Objetos
#mapear objetos do mundo real ao nosso sistema
#mapeia tabelas
#mapeia usando classes
#escopo - visibilidade das variaveis e tempo de vida das variaveis

#class Pessoa():

#    def __init__(self, nome, idade):  - metodo construtor
#       self.nome = nome
#       self.idade = idade

     #variaveis de instacia da classe
     #caracteristicas

     #self para acessar a variavel global
     #sem o self na funcao andar criara uma variavel local

     #nome = ""
     #idade = 0

     #operacoes / metodos
     #andar -
#      def andar(self):
#       self.nome = "mike"
     #doar sangue - def doarSangue():

#    Pessoa p1 = Pessoa("Mike", 21)
#    Pessoa p2 = Pessoa("Livs", 21)


class Pessoa:
    def __init__(self, nome :str, idade: int | None, esporte: str,):
        self.nome = nome
        self.idade = idade
        self.esporte = esporte

pessoa1 = Pessoa(idade = 21, nome = "Mike")
pessoa2 = Pessoa("Mikes", 21, esporte = "Volei")
pessoa3 = Pessoa("Mikess", None)



