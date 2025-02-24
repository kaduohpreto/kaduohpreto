import sqlite3 

#Variável para realizar a conexão com o banco de dados
con= sqlite3.connect('dados.db')

#Tabela Usuários
con.execute('CREATE TABLE usuarios(\
                id INTEGER PRIMARY KEY, \
                nome TEXT, \
                sobrenome TEXT, \
                endereco TEXT, \
                email TEXT, \
                telefone TEXT)')

#Tabela Livros
con.execute('CREATE TABLE livros (\
                id INTEGER PRIMARY KEY, \
                titulo TEXT, \
                autor TEXT, \
                editora TEXT, \
                ano_publicacao INTEGER, \
                isbn TEXT)')

#Tabela Empréstimos
con.execute('CREATE TABLE emprestimos(\
                id INTEGER PRIMARY KEY, \
                id_livro INTEGER, \
                id_usuario INTEGER, \
                data_emprestimo TEXT, \
                data_devolucao TEXT, \
                FOREIGN KEY (id_livro) REFERENCES livros (id),\
                FOREIGN KEY (id_usuario) REFERENCES usuarios (id))')