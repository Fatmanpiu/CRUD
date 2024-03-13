
import sqlite3

banco = sqlite3.connect("banco.db")

cursor = banco.cursor()

def TabUser():
    tabela_usuario ="""
CREATE TABLE IF NOT EXISTS usuario(
    id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT NOT NULL
);
"""
    banco.commit()
    cursor.execute(tabela_usuario)


TabUser()


def Usuario():
    criar_user = """
    INSERT INTO usuario(
    usuario,
    idade,
    email)VALUES(?,?,?)
    """
    print("Escreva seu usuario:")
    usuario = str(input()) 
    while usuario == "":
        print("ERRO. escreva seu usuario:")
        usuario = str(input())

    while True:
        try:
            idade = int(input("Digite sua idade:\n"))
            break
        except ValueError:
            print("Por favor, insira um número inteiro para a idade.")
    
    
    while True:
        try:
            email = input("Escreva seu email:\n")
            break
        except ValueError:
            print("Digite um email valido.")    
    cursor.execute(criar_user,(usuario,idade,email))
    
    banco.commit()
    opoes()



def ListandoUser():
        #----LISTANDO------#
    cursor.execute("SELECT * FROM usuario")  
    
    for user in cursor.fetchall():
        print(f"ID: {user[0]}")
        print(f"Usuario: {user[1]}")
        print(f"Idade: {user[2]}")
        print(f"Email {user[3]}")
    
    banco.commit()
    opoes()
      


def DeletandoUser():
    
    deletUser = "DELETE FROM usuario WHERE id_usuario = ?"
    
    print("Digite o ID do usuario que será deletado")
    id = input()
    while id == "":
        print("Digite um ID valido")
        id = input()
    
    cursor.execute(deletUser,(id))
    print("Usuario excluido com sucesso")
    
    banco.commit()
    opoes()
    


def UpdateUsuario():
    update = "UPDATE usuario SET email = ? WHERE id_usuario = ?"
    
    while True:
        try:
            id = int(input("Digite o id do Usuario para mudar o email:\n"))
            break
        except ValueError:
            print("Por favor, insira um número inteiro do ID.")
    while True:
        try:
            print("Qual novo Email?")
            NovoEmail = input()
            break
        except ValueError:
            print("Erro!!, tente novamente")
  
          
    print("Atualização feita!")
    cursor.execute(update,(NovoEmail,id))
    banco.commit()
    opoes()
    


def opoes():
    print("1-Criar um usuario")
    print("2-Listar usuarios")
    print("3-Deletar usuario")
    print("4-Atualizar email")
    print("Qual opção você quer?")
    opcao = input()
    
    if opcao == "1":
        Usuario()
    if opcao == "2":
        ListandoUser()
    if opcao == "3":
        DeletandoUser()
    if opcao == "4":
        UpdateUsuario()
opoes()
