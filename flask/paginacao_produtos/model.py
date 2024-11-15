produtos = [ #lista dos produtos
    {'id': 1, 'nome': 'Produto 1', 'descricao': 'Descrição do Produto 1'},
    {'id': 2, 'nome': 'Produto 2', 'descricao': 'Descrição do Produto 2'},
    {'id': 3, 'nome': 'Produto 3', 'descricao': 'Descrição do Produto 3'},
    {'id': 4, 'nome': 'Produto 4', 'descricao': 'Descrição do Produto 4'},
    {'id': 5, 'nome': 'Produto 5', 'descricao': 'Descrição do Produto 5'},
    {'id': 6, 'nome': 'Produto 6', 'descricao': 'Descrição do Produto 6'},
    {'id': 7, 'nome': 'Produto 7', 'descricao': 'Descrição do Produto 7'},
    {'id': 8, 'nome': 'Produto 8', 'descricao': 'Descrição do Produto 8'},
    {'id': 9, 'nome': 'Produto 9', 'descricao': 'Descrição do Produto 9'},
    {'id': 10, 'nome': 'Produto 10', 'descricao': 'Descrição do Produto 10'}
]


def lista_produtosPag(pagina, produtos_por_pagina=3): #(numero da pag solicitada, numero de produtos exibidos em cada pagina=3 )
#PAGINAÇÃO: retorna uma parte da lista de produtos com base da pag solicitada (permite dividir uma grande lista em varias pags com numero limitado de produtos)
    inicio = (pagina - 1) * lista_produtosPag
    #calcular em que posição da lista de produtos o primeiro produto da pag vai estar
    fim = inicio + lista_produtosPag
    #calcular até qual posição a lista de produtos vai ser exibida na pag
    return produtos[inicio:fim]
    #retorna os produtos que tão no intervalo entre o 'inicio' e o 'fim'

def acharId(id): #acha um produto pelo id
    for p in produtos: #percorre a lista produtos
        if p['id'] == id: #verifica se o id do produto é igual ao id fornecido
            return p #se for verdadeiro, o produto será retornado
    return None #se for falso, nada será retornado
