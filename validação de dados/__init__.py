from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nome = "" 
    email = ""
    senha = ""
    senha2 = ""
    errors = []
    if request.method=='POST':
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        senha2 = request.form["senha2"]

        if not nome or len(nome)<3:
            errors.append('O nome deve conter no mínimo 3 caracteres.')

        if not email:
            errors.append('Insira um e-mail.')

        if not senha or len(senha)<8 or len(senha)>12 :
            errors.append('A senha deve ter entre 8 e 12 caracteres.')

        if not any(char.isdigit() for char in senha):
            errors.append('A senha deve conter pelo menos um número.')
        
        if not any(char.isupper() for char in senha):
            errors.append('A senha deve conter pelo menos uma letra maiúscula.')
        
        if not any(char in "!@#$%^&*()_+" for char in senha):
            errors.append('A senha deve conter pelo menos um caractere especial.')
        
        if (senha2!=senha):
            errors.append('As senhas não são iguais.')


    return render_template('index.html', errors=errors)


if __name__=="__main__":
    app.run(debug=True)