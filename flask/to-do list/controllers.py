from flask import Blueprint, render_template, request, redirect, url_for
from .models import tarefa, addTarefa

tarefa_controllers=Blueprint("tarefa", __name__)

@tarefa_controllers.route("/")
def index():
    return render_template('index.html', tarefas=tarefa)

@tarefa_controllers.route("/add", methods=["POST"])
def add():
    descricao = request.form["descricao"]
    addTarefa(descricao)
    return redirect(url_for('tarefa.index'))