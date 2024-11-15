from banco import Banco

nome=input("Qual o seu nome? ")
saldo=int(input("Olá {}, qual o seu saldo? R$".format(nome)))
c1=Banco(nome, saldo)
c1.mostrarSaldo()

dep=int(input("Qual quantia deseja depositar? R$"))
c1.deposito(dep)
c1.mostrarSaldo()

sac=int(input("Qual quantia deseja sacar? R$"))
c1.sacar(sac)
c1.mostrarSaldo()

emp=int(input("Qual o valor do empréstimo que deseja fazer? R$"))
vez=int(input("Em quantas prestações deseja pagar o empréstimo? R$"))
c1.empres(emp, vez)
c1.mostrarSaldo()

c1.mostrarDeve()