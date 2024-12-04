from flask import Blueprint, render_template, request, redirect
from model import BibliotecaModel

biblioteca_bp = Blueprint('biblioteca', __name__)
model = BibliotecaModel()

@biblioteca_bp.route("/")
def index():
    livros = model.listar_livros()
    autores = model.listar_autores()
    categorias = model.listar_categorias()
    return render_template("index.html", livros=livros, autores=autores, categorias=categorias)

@biblioteca_bp.route("/adicionar_livro", methods=["POST"])
def adicionar_livro():
    titulo = request.form["titulo"]
    isbn = request.form["isbn"]
    autor_id = request.form["autor_id"]
    categoria_id = request.form["categoria_id"]
    model.adicionar_livro(titulo, isbn, autor_id, categoria_id)
    return redirect("/")

@biblioteca_bp.route("/adicionar_autor", methods=["POST"])
def adicionar_autor():
    nome = request.form["nome"]
    model.adicionar_autor(nome)
    return redirect("/")

@biblioteca_bp.route("/adicionar_categoria", methods=["POST"])
def adicionar_categoria():
    nome = request.form["nome"]
    model.adicionar_categoria(nome)
    return redirect("/")

@biblioteca_bp.route("/excluir_livro/<int:livro_id>")
def excluir_livro(livro_id):
    model.excluir_livro(livro_id)
    return redirect("/")

@biblioteca_bp.route("/excluir_autor/<int:autor_id>")
def excluir_autor(autor_id):
    model.excluir_autor(autor_id)
    return redirect("/")

@biblioteca_bp.route("/excluir_categoria/<int:categoria_id>")
def excluir_categoria(categoria_id):
    model.excluir_categoria(categoria_id)
    return redirect("/")

@biblioteca_bp.route("/editar_livro/<int:livro_id>", methods=["GET", "POST"])
def editar_livro(livro_id):
    if request.method == "POST":
        titulo = request.form["titulo"]
        isbn = request.form["isbn"]
        autor_id = request.form["autor_id"]
        categoria_id = request.form["categoria_id"]
        model.atualizar_livro(livro_id, titulo, isbn, autor_id, categoria_id)
        return redirect("/")
    
    livro = model.buscar_livro(livro_id)
    autores = model.listar_autores()
    categorias = model.listar_categorias()
    return render_template("index.html", livro=livro, autores=autores, categorias=categorias, action="editar_livro")

@biblioteca_bp.route("/editar_autor/<int:autor_id>", methods=["GET", "POST"])
def editar_autor(autor_id):
    if request.method == "POST":
        nome = request.form["nome"]
        model.atualizar_autor(autor_id, nome)
        return redirect("/")
    
    autor = model.buscar_autor(autor_id)
    return render_template("index.html", autor=autor, action="editar_autor")

@biblioteca_bp.route("/editar_categoria/<int:categoria_id>", methods=["GET", "POST"])
def editar_categoria(categoria_id):
    if request.method == "POST":
        nome = request.form["nome"]
        model.atualizar_categoria(categoria_id, nome)
        return redirect("/")
    
    categoria = model.buscar_categoria(categoria_id)
    return render_template("index.html", categoria=categoria, action="editar_categoria")
