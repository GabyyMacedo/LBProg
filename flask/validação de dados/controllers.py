from flask import Blueprint, render_template, request

dados_controllers=Blueprint('dado', __name__)

@dados_controllers.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')