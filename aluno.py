class Pessoa:
    def __init__(self, nome, idade, prontuario):
        self.nome = nome
        self.idade = idade
        self.prontuario = prontuario

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Prontuário: {self.prontuario}"
class Aluno(Pessoa):
    def __init__(self, nome, idade, prontuario):
        super().__init__(nome, idade, prontuario)
        self.notas = []  

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def status(self):
        media = self.media()
        if media >= 6:
            return "Aprovado"
        elif 4.5 <= media < 6:
            return "Recuperação"
        else:
            return "Reprovado"

    def __str__(self):
        return (super().__str__() + 
                f", Notas: {self.notas}, Média: {self.media():.2f}, Status: {self.status()}")
class Professor(Pessoa):
    def __init__(self, nome, idade, prontuario, sala, materia):
        super().__init__(nome, idade, prontuario)
        self.sala = sala
        self.materia = materia

    def __str__(self):
        return super().__str__() + f", Sala: {self.sala}, Matéria: {self.materia}"

aluno = Aluno("Larissa Manoela", 18, "1234567")
aluno.adicionar_nota(7.5)
aluno.adicionar_nota(8.0)
aluno.adicionar_nota(9.0)

print(aluno)

aluno2 = Aluno("Joao Guilherme", 19, "7654321")
aluno2.adicionar_nota(5.0)
aluno2.adicionar_nota(4.0)
aluno2.adicionar_nota(6.0)

print(aluno2)

professor = Professor("Igor", 25, "456789", "Sala 101", "Laboratório de programação")

print(professor)