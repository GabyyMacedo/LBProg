from flask import Flask, g
import sqlite3
from controller import biblioteca_bp

app = Flask(__name__)
app.register_blueprint(biblioteca_bp)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('biblioteca.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
