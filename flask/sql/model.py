import sqlite3

class BibliotecaModel:
    def __init__(self):
        self.conexao = sqlite3.connect("biblioteca.db", check_same_thread=False)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            autor_id INTEGER,
            categoria_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES Autores (id),
            FOREIGN KEY (categoria_id) REFERENCES Categorias (id)
        )
        """)
        self.conexao.commit()

    def listar_livros(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        SELECT Livros.id, Livros.titulo, Livros.isbn, Autores.nome AS autor, Categorias.nome AS categoria
        FROM Livros
        LEFT JOIN Autores ON Livros.autor_id = Autores.id
        LEFT JOIN Categorias ON Livros.categoria_id = Categorias.id
        """)
        return cursor.fetchall()

    def listar_autores(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Autores")
        return cursor.fetchall()

    def listar_categorias(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Categorias")
        return cursor.fetchall()

    def adicionar_livro(self, titulo, isbn, autor_id, categoria_id):
        cursor = self.conexao.cursor()
        cursor.execute("""
        INSERT INTO Livros (titulo, isbn, autor_id, categoria_id)
        VALUES (?, ?, ?, ?)
        """, (titulo, isbn, autor_id, categoria_id))
        self.conexao.commit()

    def adicionar_autor(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Autores (nome) VALUES (?)", (nome,))
        self.conexao.commit()

    def adicionar_categoria(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Categorias (nome) VALUES (?)", (nome,))
        self.conexao.commit()

    def excluir_livro(self, livro_id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM Livros WHERE id = ?", (livro_id,))
        self.conexao.commit()

    def buscar_livro(self, livro_id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Livros WHERE id = ?", (livro_id,))
        return cursor.fetchone()

    def buscar_autor(self, autor_id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Autores WHERE id = ?", (autor_id,))
        return cursor.fetchone()

    def buscar_categoria(self, categoria_id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Categorias WHERE id = ?", (categoria_id,))
        return cursor.fetchone()

    def atualizar_livro(self, livro_id, titulo, isbn, autor_id, categoria_id):
        cursor = self.conexao.cursor()
        cursor.execute("""
        UPDATE Livros SET titulo = ?, isbn = ?, autor_id = ?, categoria_id = ?
        WHERE id = ?
        """, (titulo, isbn, autor_id, categoria_id, livro_id))
        self.conexao.commit()

    def atualizar_autor(self, autor_id, nome):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE Autores SET nome = ? WHERE id = ?", (nome, autor_id))
        self.conexao.commit()

    def atualizar_categoria(self, categoria_id, nome):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE Categorias SET nome = ? WHERE id = ?", (nome, categoria_id))
        self.conexao.commit()
