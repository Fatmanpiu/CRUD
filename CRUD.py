import sqlite3
banco = sqlite3.connect('banco.db')
banco2 = sqlite3.connect('assunto.db')

cursor = banco.cursor()
cursor2 = banco2.cursor()


def TabAssunto():
    
    #cursor2.execute("SELECT 'Genero' FROM sqlite_master WHERE type='table' ")
    cursor2.execute("PRAGMA table_info(Genero)")
    table_info = cursor2.fetchall()

    if not table_info:
    
        tabela_assunto = """
            CREATE TABLE Genero(
            id_assunto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            assunto TEXT,
            publico TEXT
            
            );
        """
        cursor2.execute(tabela_assunto)

        assunts = [
            ('GAMES', 'GAMERS'),
            ('CURIOSIDADES', 'CURIOSOS'),
            ('LAZER', 'TODOS')
        ]

        cursor2.executemany("INSERT INTO Genero(assunto, publico) VALUES (?, ?)", assunts)
        banco2.commit()
TabAssunto()


tabela_post = """
CREATE TABLE IF NOT EXISTS post(
    id_post INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    autor  TEXT,
    conteudo TEXT,
    id_assuntos_post INTEGER,
    assunto TEXT,
    FOREIGN KEY (id_assuntos_post) REFERENCES Genero(id_assunto)
    
);
"""
banco.commit()
cursor.execute(tabela_post)

def CriandoPost():  
    crindo_post = """
    INSERT INTO post(autor,conteudo,id_assuntos_post,assunto)VALUES(?,?,?,?)
    """

    print("Quem está escrevendo?")
    autor = input()
    if autor == "":
        print("Erro, escreva o nome do autor!")
        return CriandoPost()
    print("Escreva um post")
    conteudo = input()
    while conteudo == "":
        print("Erro,escreva um conteudo")
        print("Escreva um post")
        conteudo = input()
    cursor2.execute("SELECT * FROM Genero")
    for a in cursor2.fetchall():
        print(f"ID: {a[0]} - Assuntos: {a[1]}") 

    while True:
        try:
            print("Escreva o ID do assunto")
            id_a = int(input())
            break
        except ValueError:
            print("ID INVALIDO!!")
    while id_a >= 4 or id_a < 1:
        print("ERRO! tente novamente")
        print("Escreva o ID do assunto")
        id_a = int(input())
    id_assuntos_post = str(id_a)
    cursor2.execute("SELECT assunto FROM Genero WHERE id_assunto = ?", (id_assuntos_post))
    for i in cursor2.fetchall():
        assunto = i[0]
    cursor.execute(crindo_post,(autor,conteudo,id_assuntos_post,assunto))
    
    #inserindo no banco
    banco.commit()
    
    opcao()
    
    

def ListandoPost():
    
    
    cursor.execute(tabela_post)
    cursor.execute("SELECT * FROM post")
    
            #converte as informações em um array
    for p in cursor.fetchall():
         print(f"ID:{p[0]}")
         print(f"Autor:{p[1]}")
         print(f"Conteudo:{p[2]}")
         print(f"Assunto:{p[4]}")
    

    banco.commit()
    print(50 * '-')
    print("Digite 's' para continuar...")
    passe = input()
    if passe == "s":
        opcao()
    else:
        print("Não foi digitado 's'")
        ListandoPost()


def AniquilandoPost():
    
    
    cursor.execute(tabela_post)
    destruir = "DELETE FROM post WHERE id_post = ?"

    while True:
        try:
            print("\nID do post que será excluido:")
            id = int(input())
            break
        except ValueError: 
            print("Numero invalido, tente novamente")
    I = str(id)        
    cursor.execute(destruir, (I))
    print("O post foi excluido com sucesso")



    banco.commit()
    
    opcao()


def MaisUmaChance():
    
    
    cursor.execute(tabela_post)
    Up = "UPDATE post SET conteudo = ? WHERE id_post = ?"
    
    while True:
        try:
            print("Qual o id do post que você quer mudar?")
            id = int(input())
            break
        except ValueError: 
            print("Numero invalido, tente novamente")  
    I = str(id)
    while True:
        try:
            print("Qual novo conteudo?")
            NovoConteudo = input()
            break
        except ValueError:
            print("Numero invalido, tente novamente")
            
    print("Atualização feita!")
    cursor.execute(Up, (NovoConteudo,I))
    banco.commit()
    
    opcao()
   


def opcao():
    print("Digite 1: Novo post")
    print("Digite 2: Mostrar os posts")
    print("Digite 3: Delete um post")
    print("Digite 4: Mude um post")
    print(50 * '-')
    while True:
        try:
            print("\nDigite o numero da opção desejada:")
            n = int(input())
            break
        except ValueError: 
            print("Numero invalido, tente novamente")    


    while n >= 5 or n < 1:
        print("Não existe essa opção")
        opcao()
    
    if n == 1:
     CriandoPost()
    
    elif n == 2:
        ListandoPost()
    elif n == 3:
     AniquilandoPost()
    elif n == 4:
   	 MaisUmaChance()
   
    

opcao()