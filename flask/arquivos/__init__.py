from flask import Flask
from .controllers import tarefa_controllers
app = Flask(__name__)
app.register_blueprint(tarefa_controllers)
if __name__=="__main__":
    app.run(debug=True)