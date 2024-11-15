class Pessoas:
    def __init__(self, nome, cpf, endereco, telefone, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__end = endereco
        self.__tel = telefone
        self.__email = email

    def exibir(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Endereço: {self.__end}, Telefone: {self.__tel}, E-mail: {self.__email}"

class Funcionario(Pessoas):
    def __init__(self, nome, cpf, endereco, telefone, email, salario):
        super().__init__(nome, cpf, endereco, telefone, email)
        self.__sal = salario
        self.__ativo = True

    def contratar(self):
        if not self.__ativo:
            self.__ativo = True
            return f"{self.__nome} foi contratado."
        else:
            return f"{self.__nome} está contratada."

    def demitir(self):
        if self.__ativo:
            self.__ativo = False
            return f"{self.__nome} foi demitido."
        else:
            return f"{self.__nome} já está demitido."

class cliente(Pessoas):
    def __init__(self, nome, cpf, endereço, telefone, email):
        super().__init__(nome, cpf, endereço, telefone, email)

    def exibir(self):
        return super().exibir()


class Obra:
    def __init__(self, nome, isbn, editora, edicao, estoque):
        self.__nome = nome
        self.__edicao = edicao
        self.__editora = editora
        self.__isbn = isbn
        self.__estoque = estoque


class Livro(Obra):
    def __init__(self, nome, isbn, autor, editora, edicao, data, estoque):
        super().__init__(nome, isbn, editora, edicao, estoque)
        self.__autor = autor
        self.__data = data

    def emprestimo(self, data_emprestimo):
        if self.__estoque > 0:
            self.__estoque -= 1
            print(f"Livro '{self.__nome}' emprestado em {data_emprestimo}. Estoque restante: {self.__estoque}")
        else:
            print(f"Não há estoque disponível para o livro '{self.__nome}'.")

    def mostrar_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"ISBN: {self.__isbn}")
        print(f"Autor: {self.__autor}")
        print(f"Editora: {self.__editora}")
        print(f"Edição: {self.__edicao}")
        print(f"Ano: {self.__data}")
        print(f"Estoque: {self.__estoque}")

    def Devolucao(self, estado, avaliacao):
        if estado <= 2:
            self.__estoque -= 1
            print(
                f"O livro '{self.__nome}' foi devolvido em mau estado. Estoque atual: {self.__estoque}. Multa de R$100 aplicada.")
        else:
            self.__estoque += 1
            print(f"O livro '{self.__nome}' foi devolvido em bom estado. Estoque atual: {self.__estoque}.")

        print(f"Avaliação do livro '{self.__nome}': {avaliacao}/10")

livros_dados = [
    ["Dom Quixote", "1", "Miguel de Cervantes", "Editorial Clássicos", "1ª edição", 1605, 3],
    ["1984", "2", "George Orwell", "Penguin Books", "1ª edição", 1949, 6],
    ["Orgulho e Preconceito", "3", "Jane Austen", "Penguin Classics", "1ª edição", 1813, 2],
    ["Cem Anos de Solidão", "4", "Gabriel García Márquez", "HarperCollins", "1ª edição", 1967, 1],
    ["Harry Potter e a Pedra Filosofal", "5", "J.K. Rowling", "Bloomsbury Publishing", "1ª edição", 1997, 9],
    ["O Senhor dos Anéis: A Sociedade do Anel", "6", "J.R.R. Tolkien", "Houghton Mifflin", "1ª edição", 1954, 8],
    ["Crime e Castigo", "7", "Fiódor Dostoiévski", "Editora 34", "1ª edição", 1866, 5],
    ["A Revolução dos Bichos", "8", "George Orwell", "Companhia das Letras", "1ª edição", 1945, 15],
    ["O Pequeno Príncipe", "9", "Antoine de Saint-Exupéry", "Agir", "1ª edição", 1943, 25],
    ["O Apanhador no Campo de Centeio", "10", "J.D. Salinger", "Little, Brown and Company", "1ª edição", 1951, 11]
]

livros = []
for livro_dados in livros_dados:
    livro = Livro(*livro_dados)
    livros.append(livro)
def cadastrar_novo_livro(lista_livros):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    edicao = input("Digite a edição do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    estoque = int(input("Digite a quantidade em estoque do livro: "))

    novo_livro = Livro(nome, isbn, editora, edicao, estoque, autor, None)
    lista_livros.append(novo_livro)
    print("Livro Cadastrado com Sucesso!")

    ultimo_livro = livros[-1]
    print("\nNovo livro cadastrado:")
    print("Nome:", ultimo_livro.nome)
    print("Autor:", ultimo_livro.autor)
    print("Estoque:", ultimo_livro.estoque)
    print("Total de livros na lista:", len(livros))

class Revista(Obra):
    def __init__(self, nome, isbn, editora,edicao,estoque):
        super().__init__(nome, isbn, editora, edicao,estoque)
    def emprestimoR(self, data_emprestimo):
        if self.__estoque > 0:
            self.__estoque -= 1
            print(f"Revista '{self.__nome}' emprestada em {data_emprestimo}. Estoque restante: {self.__estoque}")
        else:
            print(f"Não há estoque disponível para a revista '{self.__nome}'.")

    def mostrar_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"ISBN: {self.__isbn}")
        print(f"Autor: {self.__autor}")
        print(f"Editora: {self.__editora}")
        print(f"Edição: {self.__edicao}")
        print(f"Ano: {self.__data}")
        print(f"Estoque: {self.__estoque}")

    def DevolucaoR(self, estado, avaliacao):
        if estado <= 2:
            self.__estoque -= 1
            print(
                f"A Revista '{self.__nome}' foi devolvida em mau estado. Estoque atual: {self.__estoque}. Multa de R$50 aplicada.")
        else:
            self.__estoque += 1
            print(f"A Revista '{self.__nome}' foi devolvida em bom estado. Estoque atual: {self.__estoque}.")

        print(f"Avaliação da revista '{self.__nome}': {avaliacao}/10")
revistas_dados = [
    ["National Geographic", "1", "National Geographic Society", "Março de 2022", 1],
    ["Time", "2","Time USA, LLC", "Fevereiro de 2024", 9],
    ["Scientific American", "3","Springer Nature", "Janeiro de 2024", 16],
    ["The Economist","4", "The Economist Group", "Abril de 2023", 7],
    ["Vogue","5", "Condé Nast", "Maio de 2022", 13]
]
revistas = []
for revista_dados in revistas_dados:
    revista = Revista(*revista_dados)
    revistas.append(revista)

def cadastrar_nova_revista(lista_revistas):
    nome = input("Digite o nome da revista: ")
    isbn=input("Digite o ISBN da revista")
    editora = input("Digite o nome da editora: ")
    edicao = input("Digite a edição da revista: ")
    estoque = int(input("Digite a quantidade em estoque da revista: "))

    nova_revista = Revista(nome,isbn,editora, edicao, estoque)
    lista_revistas.append(nova_revista)
    print("Revista Cadastrada com sucesso!")
    ultima_revista = revistas[-1]
    print("\nNova revista cadastrada:")
    print("Nome:", ultima_revista.nome)
    print("Editora:", ultima_revista.editora)
    print("Edição:", ultima_revista.edicao)
    print("Estoque:", ultima_revista.estoque)
    print("Total de revistas na lista:", len(revistas))


class Jornal(Obra):
    def __init__(self, nome, isbn,editora, data, estoque):
        super().__init__(nome,isbn, editora, data, estoque)
    def emprestimoJ(self, data_emprestimo):
        if self.__estoque > 0:
            self.__estoque -= 1
            print(f"Jornal '{self.__nome}' emprestado em {data_emprestimo}. Estoque restante: {self.__estoque}")
        else:
            print(f"Não há estoque disponível para o jornal '{self.__nome}'.")

    def mostrar_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"ISBN: {self.__isbn}")
        print(f"Autor: {self.__autor}")
        print(f"Editora: {self.__editora}")
        print(f"Edição: {self.__edicao}")
        print(f"Ano: {self.__data}")
        print(f"Estoque: {self.__estoque}")

    def DevolucaoJ(self, estado, avaliacao):
        if estado <= 2:
            self.__estoque -= 1
            print(
                f"O Jornal'{self.__nome}' foi devolvido em mau estado. Estoque atual: {self.__estoque}. Multa de R$30 aplicada.")
        else:
            self.__estoque += 1
            print(f"O Jornal '{self.__nome}' foi devolvido em bom estado. Estoque atual: {self.__estoque}.")

        print(f"Avaliação do Jornal '{self.__nome}': {avaliacao}/10")

jornais_data = [
        ["The New York Times","1","The New York Times Company", "14 de março de 2024", 25],
        ["The Guardian","2","Guardian Media Group", "14 de março de 2024", 37],
        ["Le Monde","3", "Groupe Le Monde", "14 de março de 2024", 28],
        ["The Times","4", "News UK", "14 de março de 2024", 53],
        ["El País","5", "PRISA", "14 de março de 2024", 13],
        ["Der Spiegel","6", "Spiegel-Verlag", "14 de março de 2024", 17],
        ["Yomiuri Shimbun", "7","The Yomiuri Shimbun Holdings", "14 de março de 2024", 43]
    ]

jornais = []
for jornal_data in jornais_data:
        jornal = Jornal(*jornal_data)
        jornais.append(jornal)
def cadastrar_novo_jornal(lista_jornais):
    nome = input("Digite o nome do jornal: ")
    isbn=input("Digite o ISBN: ")
    editora = input("Digite o nome da editora: ")
    data = input("Digite a data do jornal: ")
    estoque = int(input("Digite a quantidade em estoque do jornal: "))

    novo_jornal = Jornal(nome, isbn,editora, data, estoque)
    lista_jornais.append(novo_jornal)
    print("Jornal Cadastrado com Sucesso!")
    ultimo_jornal = jornais[-1]
    print("\nNovo jornal cadastrado:")
    print("Nome:", ultimo_jornal.nome)
    print("Editora:", ultimo_jornal.editora)
    print("Data:", ultimo_jornal.edicao)
    print("Estoque:", ultimo_jornal.estoque)
    print("Total de jornais na lista:", len(jornais))
