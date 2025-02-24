from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
from view import *
from datetime import datetime, timedelta

#Variáveis com as cores:
co0= "#2e2d2b"  #Preto
co1= "#ffffff"  #Branco
co2= "#4fa882"  #Verde
co3= "#38576b"  #Valor
co4= "#403d3d"  #Letra
co5= "#0e6636"  #Profit
co6= "#e9a178"  #
co7= "#3fbfb9"  #Verde
co8= "#263238"  #Verde
co9= "#9e9df5"  #Verde
co10= "#6e8faf" #
co11= "#f2f4f2" #

#Criando/Dimensionando janela
janela = Tk()
janela.title("BIBLIOTECA Sistema de Gerenciamento")
janela.geometry('770x400')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

#Criando os FRAMES
#Cima
frameCima = Frame(janela, width=770, height=50, bg=co6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

#Esquerda
frameEsquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

#Direita
frameDireita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

#Ícone da logo
img_logo = Image.open("IMG/icone1.png")
img_logo = img_logo.resize((40, 40))
img_logo = ImageTk.PhotoImage(img_logo)

def_logo = Label(frameCima, image=img_logo, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
def_logo.place(x=5, y=0)

logo = Label(frameCima, text="BIBLIOTECA Sistema de Gerenciamento", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
logo.place(x=50, y=7)

#Linha de borda do cabeçalho
def_linha = Label(frameCima, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
def_linha.place(x=0, y=47)

#Ícones do menu
#======================================== Novo usuário ================================================================================
img_novo_usuario = Image.open("IMG/icone2.png")
img_novo_usuario = img_novo_usuario.resize((30, 30))
img_novo_usuario = ImageTk.PhotoImage(img_novo_usuario)

#Botão: Novo usuário
b_novo_usuario = Button(frameEsquerda, command=lambda: control('novo_usuario'), image=img_novo_usuario, compound=LEFT, anchor=NW, text="Cadastrar usuário(a)", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
b_novo_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

def novo_usuario():
    global img
    def add():
        nome = dig_nome.get()
        sobrenome = dig_sobrenome.get()
        endereco = dig_endereco.get()
        email = dig_email.get()
        telefone = dig_numero.get()
        
        lista = [nome, sobrenome, endereco, email, telefone]

        #Comando para verificar se algum campo está vazio
        for i in lista:
            if i == "":
                messagebox.showerror('ERRO', 'Preencha todos os campos corretamente')
                return

        #Inserir dados para o banco de dados
        inserir_usuario(nome, sobrenome, endereco, email, telefone)
        messagebox.showinfo("SUCESSO", "Usuário(a) cadastrado(a) com sucesso")

        #Limpando os campos de entradas
        dig_nome.delete(0, END)
        dig_sobrenome.delete(0, END)
        dig_endereco.delete(0, END)
        dig_email.delete(0, END)
        dig_numero.delete(0, END)

    msg = Label(frameDireita, text="Cadastrar usuário(a)", width=50, compound=LEFT, padx=5, pady=10, font=("Verdana 12"), bg=co1, fg=co4)
    msg.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    def_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=("Verdana 1"), bg=co3, fg=co1)
    def_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    msg_nome = Label(frameDireita, text="Nome", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    dig_nome = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    msg_sobrenome = Label(frameDireita, text="Sobrenome", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    dig_sobrenome = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    msg_endereco = Label(frameDireita, text="Endereço", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    dig_endereco = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    msg_email = Label(frameDireita, text="Email", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    dig_email = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    msg_numero = Label(frameDireita, text="Número de telefone", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_numero.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    dig_numero = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_numero.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    img = Image.open("IMG/icone9.png")
    img = img.resize((25, 25))
    img = ImageTk.PhotoImage(img)

    #Botão: Cadastrar
    b_cadastrar = Button(frameDireita, command= add, image=img, compound=LEFT, width=100, anchor=NW, text="Cadastrar", bg=co1, fg=co4, font="Ivy 12", overrelief=RIDGE, relief=GROOVE)
    b_cadastrar.grid(row=7, column=1, pady=5, sticky=NSEW)

#======================================== Cadastrar livro ================================================================================
img_novo_livro = Image.open("IMG/icone3.png")
img_novo_livro = img_novo_livro.resize((30, 30))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)

#Botão: Novo livro
b_novo_livro = Button(frameEsquerda, command=lambda: control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text="Cadastrar livro", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

def novo_livro():
    global img
    def add():
        titulo = dig_titulo.get()
        autor = dig_autor.get()
        editora = dig_editora.get()
        ano_publicacao = dig_ano.get()
        isbn = dig_isbn.get()

        lista= [titulo, autor, editora, ano_publicacao, isbn]

        #Comando para verificar se algum campo está vazio
        for i in lista:
            if i == '':
                messagebox.showerror('ERRO', 'Preencha todos os campos corretamente')
                return

        #Inserir dados para o banco de dados
        inserir_livro(titulo, autor, editora, ano_publicacao, isbn)
        messagebox.showinfo("SUCESSO", "Livro cadastrado com sucesso")

        #Limpando os campos de entradas
        dig_titulo.delete(0, END)
        dig_autor.delete(0, END)
        dig_editora.delete(0, END)
        dig_ano.delete(0, END)
        dig_isbn.delete(0, END)

    msg = Label(frameDireita, text="Cadastrar livro", width=50, compound=LEFT, padx=5, pady=10, font=("Verdana 12"), bg=co1, fg=co4)
    msg.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    def_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=("Verdana 1"), bg=co3, fg=co1)
    def_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    msg_titulo = Label(frameDireita, text="Título", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_titulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    dig_titulo = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_titulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    msg_autor = Label(frameDireita, text="Autor(a)", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    dig_autor = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    msg_editora = Label(frameDireita, text="Editora", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    dig_editora = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    msg_ano = Label(frameDireita, text="Ano de publicação", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    dig_ano = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_ano.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    msg_isbn = Label(frameDireita, text="ISBN", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    msg_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    dig_isbn = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_isbn.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    img = Image.open("IMG/icone9.png")
    img = img.resize((25, 25))
    img = ImageTk.PhotoImage(img)

    #Botão: Cadastrar
    b_cadastrar = Button(frameDireita, command= add, image=img, compound=LEFT, width=100, anchor=NW, text="Cadastrar", bg=co1, fg=co4, font="Ivy 12", overrelief=RIDGE, relief=GROOVE)
    b_cadastrar.grid(row=7, column=1, pady=5, sticky=NSEW)

#======================================== Exibir todos os usuários ================================================================================
img_todos_usuarios = Image.open("IMG/icone4.png")
img_todos_usuarios = img_todos_usuarios.resize((30, 30))
img_todos_usuarios = ImageTk.PhotoImage(img_todos_usuarios)

#Botão: Visualizar usuários(as)
b_ver_usuario = Button(frameEsquerda, command=lambda: control("ver_usuarios"), image=img_todos_usuarios, compound=LEFT, anchor=NW, text="Exibir usuários(as) cadastrados(as)", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

def ver_usuarios():
    global tree
    msg = Label(frameDireita, text="Usuários(as) cadastrados(as)", width=50, compound=LEFT, padx=5, pady=18, relief=FLAT, anchor=NW, font=("Verdana 12"), bg=co1, fg=co4)
    msg.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    def_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=("Verdana 1"), bg=co3, fg=co1)
    def_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados= exibir_usuarios()
    msg_lista= ["ID", "Nome", "Sobrenome", "Endereco", "Email", "Telefone"]

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=msg_lista, show="headings")
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    
    tree.configure(yscrollcommand=vsb.set)  

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "nw", "nw", "nw"]
    h=[20, 80, 80, 120, 120, 76, 100]
    n=0

    for col in msg_lista:
        tree.heading(col, text=col, anchor=NW)
        tree.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in dados:
        tree.insert("", "end", values=item)

#======================================== Exibir todos os livros ================================================================================
img_todos_livros = Image.open("IMG/icone5.png")
img_todos_livros = img_todos_livros.resize((30, 30))
img_todos_livros = ImageTk.PhotoImage(img_todos_livros)

#Botão: Visualizar livro(s)
b_ver_livro = Button(frameEsquerda, command=lambda: control("ver_livros"), image=img_todos_livros, compound=LEFT, anchor=NW, text="Exibir livros cadastrados", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

def ver_livros():
    global tree
    msg = Label(frameDireita, text="Livros cadastrados", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=("Verdana 12"), bg=co1, fg=co4)
    msg.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    def_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    def_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = exibir_livros()
    msg_lista = ['ID', 'Titulo', 'Autor', 'Editora', 'Ano', 'ISBN']

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=msg_lista, show="headings")
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    
    tree.configure(yscrollcommand=vsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "nw", "nw", "nw"]
    h=[20,165,110,100,50,50,100]
    n=0

    for col in msg_lista:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#======================================== Realizar um empréstimo ================================================================================
img_realizar_emp = Image.open("IMG/icone6.png")
img_realizar_emp = img_realizar_emp.resize((30, 30))
img_realizar_emp = ImageTk.PhotoImage(img_realizar_emp)

#Botão: Realizar empréstimo de livro
b_emp = Button(frameEsquerda, command=lambda:control("realizar_emprestimo"), image=img_realizar_emp, compound=LEFT, anchor=NW, text="Realizar empréstimo(s) de livro(s)", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
b_emp.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

def realizar_emprestimo():
    global img
    def add():
        id_usuario = dig_usuario.get()
        id_livro = dig_livro.get()
        hoje = datetime.today().strftime('%d-%m-%Y')
        data_devolucao = None

        #Bloco para obter a data de devolução dos livros emprestados
        if opc_7dias.get():
            data_devolucao = (datetime.today() + timedelta(days=7)).strftime('%d-%m-%Y')
        elif opc_14dias.get():
            data_devolucao = (datetime.today() + timedelta(days=14)).strftime('%d-%m-%Y')
        elif opc_21dias.get():
            data_devolucao = (datetime.today() + timedelta(days=21)).strftime('%d-%m-%Y')

        lista = [id_usuario, id_livro]

        #Comando para verificar se algum campo está vazio
        for i in lista:
            if i == '':
                messagebox.showerror('ERRO', 'Preencha todos os campos corretamente')
                return

        #Inserir dados para o banco de dados
        realizar_emp(id_usuario, id_livro, hoje, data_devolucao)
        messagebox.showinfo("SUCESSO", f"Empréstimo realizado com sucesso\nData de devolução: {data_devolucao}")

        #Limpando os campos de entradas
        dig_usuario.delete(0, END)
        dig_livro.delete(0, END)
        #Desmarcando as caixas de seleção
        opc_7dias.set(False)
        opc_14dias.set(False)
        opc_21dias.set(False)

    msg = Label(frameDireita, text="Realizar empréstimo", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    msg.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    def_linha = Label(frameDireita, width=408, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    def_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    msg_usuario = Label(frameDireita, text="ID do usuário", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    msg_usuario.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    dig_usuario = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_usuario.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    msg_livro = Label(frameDireita, text="ID do livro", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    msg_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    dig_livro = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    opc_7dias= tk.BooleanVar()
    check_7dias= tk.Checkbutton(frameDireita, text="7 dias", variable=opc_7dias, bg=co1, fg=co4, font=("Ivy10"))
    check_7dias.grid(row=4, column=0, padx=5, pady=5, sticky=NW)

    opc_14dias= tk.BooleanVar()
    check_14dias= tk.Checkbutton(frameDireita, text="14 dias", variable=opc_14dias, bg=co1, fg=co4, font=("Ivy10"))
    check_14dias.grid(row=4, column=1, padx=5, pady=5, sticky=NW)

    opc_21dias= tk.BooleanVar()
    check_21dias= tk.Checkbutton(frameDireita, text="21 dias", variable=opc_21dias, bg=co1, fg=co4, font=("Ivy10"))
    check_21dias.grid(row=4, column=2, padx=5, pady=5, sticky=NW)

    img = Image.open("IMG/icone10.png")
    img = img.resize((18, 18))
    img = ImageTk.PhotoImage(img)

    #Botão: Confirmar
    b_confirmar = Button(frameDireita, command=add, image=img, compound=LEFT, width=100, anchor=NW, text="Confirmar", bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_confirmar.grid(row=7, column=1, pady=5, sticky=NSEW)

#======================================== Devolução de empréstimo ================================================================================
img_devolucao_emp = Image.open("IMG/icone7.png")
img_devolucao_emp = img_devolucao_emp.resize((30, 30))
img_devolucao_emp = ImageTk.PhotoImage(img_devolucao_emp)

#Botão: Devolução de livro
b_devolucao_emp = Button(frameEsquerda, command=lambda: control("devolucao_emp"), image=img_devolucao_emp, compound=LEFT, anchor=NW, text="Devolução de livro(s)", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
b_devolucao_emp.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

def devolucao_emp():
    global img
    def devolucao():
        id_emprestimo = dig_id_emprestimo.get()
        data_devolucao = datetime.today().strftime('%d-%m-%Y')

        lista= [id_emprestimo]

        #Comando para verificar se algum campo está vazio
        for i in lista:
            if i == "":
                messagebox.showerror('ERRO', 'Preencha todos os campos corretamente')
                return

        devolucao_livro(id_emprestimo, data_devolucao)
        messagebox.showinfo("SUCESSO", "Devolução realizada com sucesso")
        
        #Limpando o campo de entrada
        dig_id_emprestimo.delete(0, END)

    msg = Label(frameDireita, text="Devolução de Livro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    msg.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    def_linha = Label(frameDireita, width=408, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    def_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    msg_id_emprestimo = Label(frameDireita, text="ID do Empréstimo", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    msg_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    dig_id_emprestimo = Entry(frameDireita, width=25, justify='left', relief='solid')
    dig_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    img = Image.open("IMG/icone11.png")
    img = img.resize((25, 25))
    img = ImageTk.PhotoImage(img)

    #Botão: Devolver
    b_devolucao = Button(frameDireita, command=devolucao, image=img, compound=LEFT, width=100, anchor=NW, text="Devolver", bg=co1, fg=co4, font=('Ivy 12'), overrelief=RIDGE, relief=GROOVE)
    b_devolucao.grid(row=7, column=1, pady=5, sticky=NSEW)

#======================================== Livros emprestados no momento ================================================================================
img_livros_emprestados = Image.open("IMG/icone8.png")
img_livros_emprestados = img_livros_emprestados.resize((30, 30))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)

#Botão: Visualizar emprestimos ativos
b_livros_emprestados = Button(frameEsquerda, command=lambda:control("ver_emprestimos"), image=img_livros_emprestados, compound=LEFT, anchor=NW, text="Visualizar empréstimos ativos", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

def ver_emprestimos():
    global tree
    msg = Label(frameDireita, text="Empréstimos ativos", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    msg.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    def_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    def_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = []
    msg_lista = ["ID", "Título", "Nome do usuário", "D.emprestimo", "D.devolução"]

    livros_emp = exibir_livros_emp()
    
    for livro in livros_emp:
        dado = [f"{livro[0]}", f"{livro[1]}", f"{livro[2]}", f"{livro[3]}", f"{livro[4]}"]
        dados.append(dado)

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=msg_lista, show="headings")
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    tree.configure(yscrollcommand=vsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')

    frameDireita.grid_rowconfigure(2, weight=12)

    hd = ["nw", "nw", "ne", "ne", "ne", "ne"]
    h = [30, 120, 90, 90, 100, 100]
    n = 0

    for col in msg_lista:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

#======================================== Controle do menu ================================================================================
def control(i):
    #Cadastrar usuários(as)
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_usuario()

    #Cadastrar livros
    elif i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_livro()
    
    #Exibir usuários(as)
    elif i == "ver_usuarios":
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_usuarios()
    
    #Exibir livros
    elif i == "ver_livros":
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros()

    #Realizar empréstimo
    elif i == "realizar_emprestimo":
        for widget in frameDireita.winfo_children():
            widget.destroy()
        realizar_emprestimo()

    #Exibir empréstimo(s)
    elif i == "ver_emprestimos":
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_emprestimos()
    
    #Devolução de livro(s)
    elif i == "devolucao_emp":
        for widget in frameDireita.winfo_children():
            widget.destroy()
        devolucao_emp()

def_linha = Label(frameCima, width=770, padx=5, anchor=NW, font=("Verdana 1"), bg=co3, fg=co1)
def_linha.place(x=0, y=47)

janela.mainloop()