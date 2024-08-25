from flask import Blueprint, render_template, request

alunos_controllers=Blueprint('aluno', __name__)

@alunos_controllers.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@alunos_controllers.route("/resultado", methods=["POST"])
def resultado():
    desenv = request.form.get("desenv")
    turma = request.form.get("turma")
    prof = request.form.get("prof")
    data = request.form.get("data")
    dific = request.form.get("dific")
    confiante = request.form.get("confiante")

    return render_template('resultado.html', desenv=desenv, turma=turma, prof=prof, data=data, dific=dific, confiante=confiante)
