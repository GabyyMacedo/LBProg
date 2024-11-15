from flask import render_template, jsonify, request
from model import lista_produtosPag, acharId

def lista_produtos(): #exibe a lista de produtos, com paginação
#obtém os produtos da pág atual e passa esses produtos para o template para renderizar  
    pagina = int(request.args.get('pagina', 1))
    #obtem o valor do parametro 'pagina' da URL, se não tiver o parametro, o valor padrão será 1(primeira pag)
    produtos_paginados = lista_produtosPag(pagina)
    #obtem a lista dos produtos que devem ser exibidos nqla pag. Ela divide os produtos em pág, retornando apenas os produtos da página atual 
    anterior = pagina > 1 
    # verifica se tem uma pág anterior. Se a pág atual for maior que 1, ent tem uma pág anterior
    proxima = len(produtos_paginados) == 3
    # verifica se tem uma prox pág. Se a qntd de produtos exibidos na pág atual for igual o num máx por pág, isso indica que tem mais produtos para mostrar, logo tem uma próx pág.
    return render_template('index.html', produtos=lista_produtosPag, pagina=pagina, anterior=anterior, proxima=proxima)
    #renderiza o index.html e passa as variaveis 'produto', 'pagina', 'tem_anterior', e 'tem_proxima' para o template

def detalhes_produto(id): #retorna os detalhes de um produto por JSON
#Os detalhes serao carregados via AJAX
    produto = acharId(id)
    #obtem o produto pelo id fornecido como parâmetro, se o produto for encontrado, ele vai ser retornado
    if produto: #verifica se o produto foi encontrado
        return jsonify(produto)#jsonify converte para JSON
        #se o produto for encontrado, ele vai ser retornado em formato de JSON
    return jsonify({'erro': 'Produto não encontrado'}), 404 #jsonify converte para JSON
    #se o produto não for encontrado, irá retornar uma msg de erro e um código http 404 (produto n encontardo)
