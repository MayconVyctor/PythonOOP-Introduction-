import sqlite3

class EscolaDancaForro:

    def conectarBanco(self):
        db_path = 'bancoEscolaForro.db'
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn



   # def login(self, usuario, password):

#    def inscricaoExame(self):