import sqlite3

#Função para conectar ao banco de dados
def connect():
    conn= sqlite3.connect('dados.db')
    return conn

#Função: Inserir usuários
def inserir_usuario(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone)\
                VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

#Função: Inserir livros
def inserir_livro(titulo, autor, editora, ano_publicacao, isbn):
    conn= connect()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn)\
                VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

#Função: Exibir usuários
def exibir_usuarios():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    conn.close()
    return usuarios

#Função: Exibir os livros
def exibir_livros():
    conn= connect()
    livros= conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    return livros

#Função: Realizar empréstimos
def realizar_emp(id_usuario, id_livro, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) \
                 VALUES (?,?,?,?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

#Função: Exibir livros emprestados
def exibir_livros_emp():
    conn = connect()
    resultado = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                       FROM emprestimos \
                       JOIN livros ON emprestimos.id_livro = livros.id \
                       JOIN usuarios ON emprestimos.id_usuario = usuarios.id").fetchall()

    conn.close()
    return resultado

#Função: Devolução de livros
def devolucao_livro(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao= ? WHERE id= ?",(data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

#Exemplos 
#Inserir livros (#insert_book() ):
#insert_book("Dom Quixote", "Miquel", "Editora 1", 1605, "123456")

#Inserir usuários (#exibir_usuarios() ):
#insert_user("João", "Silva", "Brasil", "teste@teste.com", "+244 123456")

#Realizar empréstimo (#insert_loan() ):
#insert_loan(1, 1, "2018-05-12", None)

#Como mostrar os livros já emprestados e a previsão de devolução
#livros_emprestados= get_books_on_loan()
#print (livros_emprestados)
#update_loan_return_date(2, "2018-06-01")
#exibir_livros()