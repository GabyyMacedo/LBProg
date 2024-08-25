from flask import Flask
from controllers import alunos_controllers
app = Flask(__name__)
app.register_blueprint(alunos_controllers)
if __name__=="__main__":
    app.run(debug=True)