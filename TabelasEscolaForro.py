import sqlite3


class TabelaEscolaForro:
    def conectarBanco(self):
        db_path = 'bancoEscolaForro.db'
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn


    def criarTabela(cur):
        cur.execute('''CREATE TABLE IF NOT EXISTS Aluno
          nome varchar NOT NULL,
          matricula integer PRIMARY KEY,
          id_turma integer NOT NULL,
          id_inscricao_exame integer NOT NULL,
          usuario_id varchar NOT NULL,
          FOREIGN KEY (id_turma) REFERENCES turma(id)
          FOREIGN KEY (id_inscricao_exame) REFERENCES incricao_exame(id)
          FOREIGN KEY (usuario) REFERENCES usuario(id)
         (''')
        cur.execute ('''CREATE TABLE IF NOT EXISTS Aluno''')


