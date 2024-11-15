from flask import Flask
from controller import lista_produtos, detalhes_produto

app = Flask(__name__)

app.add_url_rule('/produtos', 'lista_produtos', lista_produtos)
#add_url_rule(caminho da url, nome da rota, função q sera chamada qnd a rota for acessada)
#rota para lista de produtos

app.add_url_rule('/produto/<int:id>', 'detalhes_produto', detalhes_produto)
#/produto/<int:id --> exemplo: /produto/1, o 1 é um valor para o id
#rota para os detalhes dos produtos, identificados pelo id

if __name__ == '__main__':
    app.run(debug=True)