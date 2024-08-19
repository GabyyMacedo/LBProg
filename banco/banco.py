class Banco:
    def __init__(self,nome,saldo):
        self.nome=nome
        self.saldo=saldo
        self.deve=0
    
    def deposito(self,dep):
        self.saldo+=dep

    def mostrarSaldo(self):
        print(f"Seu saldo atual eh R$ {self.saldo}")

    def sacar(self, sac):
        self.saldo-=sac
    
    def empres(self, emp, vez):
        self.deve=emp+(vez*1/100)
        self.saldo+=emp

    def mostrarDeve(self):
        print(f"Você terá que pagar R$ {self.deve}")

        






    
