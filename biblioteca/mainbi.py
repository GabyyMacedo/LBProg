from biblioteca import *
print("Digite 1 para funcionário e 2 para proprietário")
quem = int(input("Quem está acessando?\n1: Funcionário\n2: Proprietário\n"))
while quem in [1, 2]:
    if quem == 1:
        while True:
            fazer = int(input(
            "O que você quer fazer?(Digite o número correspondente ao ato)\n1:Empréstimo\n2:Devolução\n3:Cadastrar livro\n "))
            while True:
                if fazer == 1:
                    while True:
                        novo = int(input("\nO empréstimo será feito para:\n1: Cliente da casa\n2: Cliente novo\n"))
                        while True:
                            if novo == 1:
                                cli = (input("\nQual o nome do cliente? "))
                                while True:
                                    tipo = int(input(
                                        "Digite o tipo de item a ser emprestado (1 para livro, 2 para revista, 3 para jornal): "))
                                    if tipo == 1:
                                        livro=livros[0]
                                        print("Qual livro será emprestado? ")
                                        isbn = input("1-Dom Quixote\n2-1984\n3-Orgulho e Preconceito\n4-Cem Anos de Solidão\n5-Harry Potter e a Pedra Filosofal\n6-Senhor dos Aneis:A Sociedade do Anel\n7-Crime e Castigo\n8-A revolução dos Bichos\n 9-Pequeno Príncipe\n10- O apanhador no Campo de Centeio\n")
                                        data_emprestimo = input("Data do empréstimo: ")
                                        aten = input("Qual funcionário está realizando o empréstimo? ")
                                        livro_encontrado= False
                                        for livro in livros:
                                            if livro.isbn == isbn:
                                                livro_encontrado = True
                                                livro.emprestimo(data_emprestimo)
                                        if not livro_encontrado:
                                            print("ISBN não encontrado.")
                                        break

                                    elif tipo == 2:
                                        revista=revistas[0]
                                        print("Qual revista será emprestada? ")
                                        isbn = input(
                                            "1-National Geographic\n2-Time\n3-Scientific American\n4-The Economistic\n5-Vogue:")
                                        data = input("Data do empréstimo: ")
                                        aten = input("Qual funcionário está realizando o empréstimo? ")
                                        revista_encontrada=False
                                        for revista in revistas:
                                            if revista.isbn == isbn:
                                                revista_encontrada = True
                                                revista.emprestimoR(data)
                                        if not revista_encontrada:
                                                print("ISBN não encontrado.")

                                        break

                                    elif tipo == 3:
                                        print("Qual jornal será emprestado? ")
                                        isbn = input("1-New Work Times\n2-The Guardian\n Le Monde\n 3-The Times\n 4-El País\n 5-Der Spiegel\n 6-Yomiuri Shimbun:")
                                        data = input("Data do empréstimo: ")
                                        aten = input("Qual funovo in [1, 2]ncionário está realizando o empréstimo? ")
                                        jornal_encontrado=False
                                        for jornal in jornais:
                                            if jornal.isbn == isbn:
                                                jornal_encontrado = True
                                                jornal.emprestimoJ(data)
                                        if not jornal_encontrado:
                                                print("ISBN não encontrado.")
                                        break
                                    else:
                                        print("Tipo inválido. Por favor, digite 1, 2 ou 3.")
                                break
                            if novo == 2:
                                print("\nVamos fazer o cadastro do novo cliente!")
                                print("Precisaremos dos seguintes dados!")
                                cli = (input("\nNome: "))
                                cpf = float(input("\nCPF: "))
                                end = (input("\nEndereço: "))
                                tel = int(input("\nTelefone: "))
                                email = input("\nE-mail: ")
                                print("\nCadastro realizado!\n")
                                while True:
                                    tipo = int(input("Digite o tipo de item a ser emprestado (1 para livro, 2 para revista, 3 para jornal): "))
                                    if tipo == 1:

                                        print("Qual livro será emprestado? ")
                                        isbn = input( "1-Dom Quixote\n 2-1984\n  3-Orgulho e Preconceito\n 4-Cem Anos de Solidão\n 5-Harry Potter e a Pedra Filosofal\n6-Senhor dos Aneis:A Sociedade do Anel\n7-Crime e Castigo\n 8-A Revolução dos Bichos\n 9-Pequeno Príncipe\n10- O apanhador no Campo de Centeio\n")
                                        data_emprestimo = input("Data do empréstimo: ")
                                        aten = input("Qual funcionário está realizando o empréstimo? ")
                                        livro_encontrado = False
                                        for livro in livros:
                                            if livro.isbn == isbn:
                                                livro_encontrado = True
                                                livro.emprestimo(data_emprestimo)
                                                break
                                        if not livro_encontrado:
                                            print("ISBN não encontrado.")
                                        break
                                    elif tipo == 2:

                                        print("Qual revista será emprestada? ")
                                        isbn = input(
                                            "1-National Geographic\n2-Time\n3-Scientific American\n 4-The Economistic\n5-Vogue")
                                        data = input("Data do empréstimo: ")
                                        aten = input("Qual funcionário está realizando o empréstimo? ")
                                        revista_encontrada=False
                                        for revista in revistas:
                                            if revista.isbn == isbn:
                                                revista_encontrada = True
                                                revista.emprestimoR(data)
                                        if not revista_encontrada:
                                                print("ISBN não encontrado.")
                                        break
                                    elif tipo == 3:
                                        print("Qual jornal será emprestado? ")
                                        isbn = input(
                                            "1-New Work Times\n2-The Guardian\n 3-Le Monde\n 4-The Times\n 5-El País\n 6-Der Spiegel\n 7-Yomiuri Shimbun:")
                                        data = input("Data do empréstimo: ")
                                        aten = input("Qual funovo in [1, 2]ncionário está realizando o empréstimo? ")
                                        jornal_encontrado=False
                                        for jornal in jornais:
                                            if jornal.isbn == isbn:
                                                jornal_encontrado = True
                                                jornal.emprestimoJ(data)
                                        if not jornal_encontrado:
                                                print("ISBN não encontrado.")
                                        break
                                    else:
                                        print("Tipo inválido. Por favor, digite 1, 2 ou 3.")
                        break
                    break
                if fazer==2:
                    d=int(input("O que gostaria de devolver?[1-Livro,2-Revista 3-jornal]"))
                    if d == 1:
                        isbn = input("Digite o ISBN do livro a ser devolvido:\n1-Dom Quixote\n2-1984\n3-Orgulho e Preconceito\n4-Cem Anos de Solidão\n5-Harry Potter e a Pedra Filosofal\n6-Senhor dos Aneis:A Sociedade do Anel\n7-Crime e Castigo\n8-A Revolução dos Bichos\n9-Pequeno Príncipe\n10- O apanhador no Campo de Centeio\n")
                        estado = int(input("Digite o estado do livro:\n1-muito ruim\n2-ruim\n3-razoável\n4-bom\n5-muito bom: "))
                        avaliacao = int(input("Digite sua avaliação do livro (de 0 a 10): "))
                        livro_encontrado = False
                        for livro in livros:
                            if livro.isbn == isbn:
                                livro_encontrado = True
                                livro.Devolucao(estado, avaliacao)
                        if not livro_encontrado:
                            print("ISBN não encontrado.")
                        break
                    elif 2 == d:
                        isbn = input("Digite o ISBN da revista a ser devolvido:\n1-National Geographic\n2-Time\n3-Scientific American\n4-The Economistic\n5-Vogue:")
                        estado = int(input("Digite o estado da revista (1-muito ruim, 2-ruim, 3-razoável, 4-bom, 5-muito bom): "))
                        avaliacao = int(input("Digite sua avaliação da revista (de 0 a 10): "))
                        revista_encontrada=False
                        for revista in revistas:
                            if revista.isbn == isbn:
                                revista_encontrada = True
                                revista.DevolucaoR(estado, avaliacao)
                                break
                        if not revista_encontrada:
                            print("ISBN não encontrado.")
                        break
                    elif d== 3:
                        isbn = input("Digite o ISBN do Jornal a ser devolvido:\n1-New Work Times\n2-The Guardian\n Le Monde\n3-The Times\n4-El País\n5-Der Spiegel\n6-Yomiuri Shimbun: ")
                        estado = int(input("Digite o estado do jornal (1-muito ruim, 2-ruim, 3-razoável, 4-bom, 5-muito bom): "))
                        avaliacao = int(input("Digite sua avaliação do jornal (de 0 a 10): "))
                        jornal_encontrado=False
                        for jornal in jornais:
                            if jornal.isbn == isbn:
                                jornal_encontrado = True
                                jornal.DevolucaoJ(estado, avaliacao)
                    else:
                        print("Digite uma opção válida!")
                    break
                if fazer == 3:
                    produto = int(input("\nDigite 1 para cadastrar livro\nDigite 2 para cadastrar revista\nDigite 3 para cadastrar jornal\n "))
                    if produto == 1:
                            cadastrar_novo_livro(livros)
                    elif produto == 2:
                             cadastrar_nova_revista(revistas)
                    elif produto == 3:
                              cadastrar_novo_jornal(jornais)
                    else:
                            print("Escolha uma opção válida!")
                else:
                        print("Digite uma opção válida!")
            break
    elif quem == 2:
        fazer = int(input("\nO que você quer fazer?(Digite o número correspondente ao ato)\n1:Empréstimo\n2:Devolução\n3:Cadastrar Produto\n4:Demitir funcionário\n5:Contratar funcionário\n6:Informações sobre Produtos\n"))
    while True:
        if fazer == 1:
            novo = int(input("\nO empréstimo será feito para:\n1: Cliente da casa\n2: Cliente novo\n"))
            while True:
                if novo == 1:
                    cli = (input("\nQual o nome do cliente? "))
                    while True:
                        tipo = int(input(
                            "Digite o tipo de item a ser emprestado (1 para livro, 2 para revista, 3 para jornal): "))

                        if tipo == 1:
                            print("Qual livro será emprestado? ")
                            isbn = input(
                                "1-Dom Quixote\n2-1984\n3-Orgulho e Preconceito\n4-Cem Anos de Solidão\n5-Harry Potter e a Pedra Filosofal\n6-Senhor dos Aneis:A Sociedade do Anel\n7-Crime e Castigo\n 8-A Revolução dos Bichos\n 9-Pequeno Príncipe\n10- O apanhador no Campo de Centeio\n")
                            data_emprestimo = input("Data do empréstimo: ")
                            aten = input("Qual funcionário está realizando o empréstimo? ")
                            for livro in livros:
                                if livro.isbn == isbn:
                                    livro_encontrado = True
                                    livro.emprestimo(data_emprestimo)
                                if not livro_encontrado:
                                    print("ISBN não encontrado.")
                            break
                        elif tipo == 2:
                            print("Qual revista será emprestada? ")
                            isbn = input(
                                "1-National Geographic\n2-Time\n3-Scientific American\n 4-The Economistic\n5-Vogue")
                            data = input("Data do empréstimo: ")
                            aten = input("Qual funcionário está realizando o empréstimo? ")
                            for revista in revistas:
                                if revista.isbn == isbn:
                                    revista_encontrada = True
                                    revista.emprestimoR(data)
                                if not revista_encontrada:
                                    print("ISBN não encontrado.")
                            break
                        elif tipo == 3:
                            print("Qual jornal será emprestado? ")
                            isbn = input(
                                "1-New Work Times\n2-The Guardian\n Le Monde\n 3-The Times\n 4-El País\n 5-Der Spiegel\n 6-Yomiuri Shimbun:")
                            data = input("Data do empréstimo: ")
                            aten = input("Qual funovo in [1, 2]ncionário está realizando o empréstimo? ")
                            for jornal in jornais:
                                if jornal.isbn == isbn:
                                    jornal_encontrado = True
                                    jornal.emprestimoJ(data)
                                if not jornal_encontrado:
                                    print("ISBN não encontrado.")
                            break
                        else:
                            print("Tipo inválido. Por favor, digite 1, 2 ou 3.")
                    break
                elif novo == 2:
                    print("\nVamos fazer o cadastro do novo cliente!")
                    print("Precisaremos dos seguintes dados!")
                    cli = (input("\nNome: "))
                    cpf = float(input("\nCPF: "))
                    end = (input("\nEndereço: "))
                    tel = int(input("\nTelefone: "))
                    email = input("\nE-mail: ")
                    print("\nCadastro realizado!\n")
                    tipo = int(input("O que vamos emprestar?\n1: Livro\n2: Revista\n3: Jornal\n"))
                    while True:
                        tipo = int(input(
                            "Digite o tipo de item a ser emprestado (1 para livro, 2 para revista, 3 para jornal): "))

                        if tipo == 1:
                            print("Qual livro será emprestado? ")
                            isbn = input(
                                "1-Dom Quixote\n 2-1984\n  3-Orgulho e Preconceito\n 4-Cem Anos de Solidão\n 5-Harry Potter e a Pedra Filosofal\n6-Senhor dos Aneis:A Sociedade do Anel\n7-Crime e Castigo\n 8-A Revolução dos Bichos\n 9-Pequeno Príncipe\n10- O apanhador no Campo de Centeio\n")
                            data_emprestimo = input("Data do empréstimo: ")
                            aten = input("Qual funcionário está realizando o empréstimo? ")
                            for livro in livros:
                                if livro.isbn == isbn:
                                    livro_encontrado = True
                                    livro.emprestimo(data_emprestimo)
                                if not livro_encontrado:
                                    print("ISBN não encontrado.")
                            break
                        elif tipo == 2:
                            print("Qual revista será emprestada? ")
                            isbn = input(
                                "1-National Geographic\n2-Time\n3-Scientific American\n 4-The Economistic\n5-Vogue")
                            data = input("Data do empréstimo: ")
                            aten = input("Qual funcionário está realizando o empréstimo? ")
                            for revista in revistas:
                                if revista.isbn == isbn:
                                    revista_encontrada = True
                                    revista.emprestimoR(data)
                                if not revista_encontrada:
                                    print("ISBN não encontrado.")
                            break

                        elif tipo == 3:
                            print("Qual jornal será emprestado? ")
                            isbn = input("\n1-New Work Times\n2-The Guardian\n3-Le Monde\n4-The Times\n5-El País\n6-Der Spiegel\n7-Yomiuri Shimbun:")
                            data = input("Data do empréstimo: ")
                            aten = input("Qual funovo in [1, 2]ncionário está realizando o empréstimo? ")
                            for jornal in jornais:
                                if jornal.isbn == isbn:
                                    jornal_encontrado = True
                                    jornal.emprestimoJ(data)
                                if not jornal_encontrado:
                                    print("ISBN não encontrado.")
                            break
                        else:
                            print("Tipo inválido. Por favor, digite 1, 2 ou 3.")
                    break
            break
        if fazer ==2:
            d = int(input("O que gostaria de devolver?[1-Livro,2-Revista 3-jornal]"))
            if d == 1:
                isbn = input(
                    "Digite o ISBN do livro a ser devolvido:\n1-Dom Quixote\n2-1984\n3-Orgulho e Preconceito\n4-Cem Anos de Solidão\n5-Harry Potter e a Pedra Filosofal\n6-Senhor dos Aneis:A Sociedade do Anel\n7-Crime e Castigo\n8-A Revolução dos Bichos\n9-Pequeno Príncipe\n10- O apanhador no Campo de Centeio\n")
                estado = int(input("Digite o estado do livro:\n1-muito ruim\n2-ruim\n3-razoável\n4-bom\n5-muito bom: "))
                avaliacao = int(input("Digite sua avaliação do livro (de 0 a 10): "))
                livro_encontrado = False
                for livro in livros:
                    if livro.isbn == isbn:
                        livro_encontrado = True
                        livro.Devolucao(estado, avaliacao)
                if not livro_encontrado:
                    print("ISBN não encontrado.")
                break
            elif 2 == d:
                isbn = input(
                    "Digite o ISBN da revista a ser devolvido:\n1-National Geographic\n2-Time\n3-Scientific American\n4-The Economistic\n5-Vogue:")
                estado = int(
                    input("Digite o estado da revista (1-muito ruim, 2-ruim, 3-razoável, 4-bom, 5-muito bom): "))
                avaliacao = int(input("Digite sua avaliação da revista (de 0 a 10): "))
                revista_encontrada = False
                for revista in revistas:
                    if revista.isbn == isbn:
                        revista_encontrada = True
                        revista.DevolucaoR(estado, avaliacao)
                        break
                if not revista_encontrada:
                    print("ISBN não encontrado.")
                break
            elif d == 3:
                isbn = input(
                    "Digite o ISBN do Jornal a ser devolvido:1-New Work Times\n2-The Guardian\n Le Monde\n 3-The Times\n 4-El País\n 5-Der Spiegel\n 6-Yomiuri Shimbun: ")
                estado = int(
                    input("Digite o estado do jornal (1-muito ruim, 2-ruim, 3-razoável, 4-bom, 5-muito bom): "))
                avaliacao = int(input("Digite sua avaliação do jornal (de 0 a 10): "))
                jornal_encontrado = False
                for jornal in jornais:
                    if jornal.isbn == isbn:
                        jornal_encontrado = True
                        jornal.DevolucaoJ(estado, avaliacao)
            else:
                print("Digite uma opção válida!")
            break
        if fazer == 3:
            produto = int(input("Digite 1 para cadastrar livro\n Digite 2 para cadastrar revista\n Digite 3 para cadastrar jornal: "))
            if produto == 1:
                cadastrar_novo_livro(livros)
            elif produto ==2:
                cadastrar_nova_revista(revistas)
            elif produto==3:
                cadastrar_novo_jornal(jornais)
            else:
                print("Escolha uma opção válida!")
        if fazer ==4:
            nome = input("Digite o nome do funcionário: ")
            cpf = input("Digite o CPF do funcionário: ")
            endereco = input("Digite o endereço do funcionário: ")
            telefone = input("Digite o telefone do funcionário: ")
            email = input("Digite o e-mail do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))

            funcionario1 = Funcionario(nome, cpf, endereco, telefone, email, salario)
            print(funcionario1.exibir())
            print(funcionario1.demitir())
        if fazer ==5:
            nome = input("Digite o nome do novo funcionário: ")
            cpf = input("Digite o CPF do novo funcionário: ")
            endereco = input("Digite o endereço do novo funcionário: ")
            telefone = input("Digite o telefone do novo funcionário: ")
            email = input("Digite o e-mail do novo funcionário: ")
            salario = float(input("Digite o salário do novo funcionário: "))

            funcionario1 = Funcionario(nome, cpf, endereco, telefone, email, salario)
            print(funcionario1.exibir())
            print(funcionario1.contratar())
        if fazer==6:
            i=int(input("Gostaria de saber informações sobre qual produto? [1-Livro, 2-Revista, 3-Jornal]"))
            if i == 1:
                for livro in livros:
                    livro.mostrar_dados()
                    print()
            elif i == 2:
                for revista in revistas:
                    revista.mostrar_dados()
                    print()
            elif i == 3:
                for jornal in jornais:
                    jornal.mostrar_dados()
                    print()
        else:
            print("Você escolheu uma opção inexistente.")
    break