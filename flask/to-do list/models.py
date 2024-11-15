class Tarefa:
    def __init__(self,id,descricao,completo = False):
        self.id=id
        self.descricao=descricao
        self.completo=completo
tarefa=[]

def addTarefa(descricao):
    id = len(tarefa) + 1
    nova_tarefa = Tarefa(id,descricao)
    tarefa.append(nova_tarefa)