import mysql.connector

from connect_db import start_connection


mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="act_db"
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sessao")


filmeslista=[]
sessaolista=[]  
clientelista=[]

class Filme:
    def __init__(self,titulo,duracao,classificacao,indicativa):
        self.titulo=titulo
        self.duracao=duracao
        self.classificacao=classificacao
        self.indicativa=indicativa

    def ExibirInf(self):
        print(f"\nTítulo: {self.titulo}\nDuração: {self.duracao} Min.\nClassificação: {self.classificacao}\nIndicativa: {self.indicativa}")


class Sessao:
    def __init__(self,filme='',horario='',assentosdisponiveis=0):
        self.filme=filme
        self.horario=horario
        self.assentosdisponiveis=assentosdisponiveis

    def ExibirSessao():
        db = start_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM sessao")
        sessoes = cursor.fetchall()

        if not sessoes:
            print("Nenhuma sessão cadastrada.")
            cursor.close()
            db.close()
            return []

        print("\nSessões disponíveis:")
        for i, sessao in enumerate(sessoes):
            print(f"{i + 1} - {sessao['filme']} às {sessao['horario']} ({sessao['assentos_disponiveis']} assentos disponíveis)")

        cursor.close()
        db.close()
        return sessoes

    
    #metodo para venda de ingressos
    def vender_ingresso(self, quantidade):
        if quantidade <= self.assentosdisponiveis:
            self.assentosdisponiveis -= quantidade
            print(f"Ingressos vendidos: {quantidade}")
            print(f"Ingressos restantes: {self.assentosdisponiveis}")
        else:
            print("Quantidade de ingressos insuficiente!")

    def ingressos_restantes(self):
        return self.assentosdisponiveis


class Cliente:
    def __init__(self, nome, nif, ingressosComprados):
        self.nome = nome
        self.nif = nif
        self.ingressosComprados = ingressosComprados

    def ExibirCliente():
        db = start_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()

        if not clientes:
            print("Nenhuma cliente cadastrado.")
            cursor.close()
            db.close()
            return []

        print("\nSessões disponíveis:")
        for i, cliente in enumerate(clientes):
            print(f"{i + 1} - Nome: {cliente['nome']} | NIF: {cliente['NIF']} | Ingressos Comprados: {cliente['ingressos_comprados']} | Sessão:{cliente['sessao_id']}")

        cursor.close()
        db.close()
        return cliente


class Cinema:
    def __init__(self,listadeSessoes):
        self.listadeSessoes=listadeSessoes
        
#Criar sessões e adiciona na lista de sessões
def Sessoesfilme():
   
    filme=str(input("\nFilme: "))
    horario=input("Horário: ")
    assentosdisponiveis=int(input("Total de assentos: "))

    def insert_db(mydb, mycursor):
        try:
            sql = "INSERT INTO `sessao`(`filme`, `horario`, `assentos_disponiveis`) VALUES (%s,%s,%s)"

            valores = (filme,horario,assentosdisponiveis)

            mycursor.execute(sql, valores)
            mydb.commit()

            print("Registo inserido com sucesso!")
                
        except mysql.connector.Error as err:
            print(f"Erro: {err}")

    mydb = start_connection()

    mycursor = mydb.cursor()

    insert_db(mydb, mycursor)
    todasSessoes=Sessao(filme,horario,assentosdisponiveis)
    sessaolista.append(todasSessoes)
#Adiciona filme a lista de filmes
def AddFilmes():
    while True:
        titulo=str(input("\nTitulo: "))
        duracao=int(input(f"Duração: "))
        classificacao=input("Classificação: ")
        indicativa=input("Indicativa: ")
        def insert_db(mydb, mycursor):
            try:
                sql = "INSERT INTO `filmes`(`nome`, `duração`, `classificação`, `indicativa`) VALUES (%s,%s,%s,%s)"

                valores = (titulo,duracao,classificacao,indicativa)

                mycursor.execute(sql, valores)
                mydb.commit()

                print("Registo inserido com sucesso!")
                
            except mysql.connector.Error as err:
                print(f"Erro: {err}")

        mydb = start_connection()

        mycursor = mydb.cursor()

        insert_db(mydb, mycursor)
        todosfilme=Filme(titulo,duracao,classificacao,indicativa)
        filmeslista.append(todosfilme)

        Sessoesfilme()
        break
#Compra de ingresso
def ComprarIngressos():
    try:
        db = start_connection()
        cursor = db.cursor(dictionary=True)

        # Obter sessões do banco
        cursor.execute("SELECT * FROM sessao")
        sessoes = cursor.fetchall()

        if not sessoes:
            print("Nenhuma sessão cadastrada.")
            return

        print("\nSessões disponíveis:")
        for i, sessao in enumerate(sessoes):
            print(f"{i + 1} - {sessao['filme']} às {sessao['horario']} ({sessao['assentos_disponiveis']} assentos disponíveis)")

        try:
            escolha = int(input("Escolha o número da sessão desejada: ")) - 1
            if escolha < 0 or escolha >= len(sessoes):
                print("Sessão inválida.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        sessao_escolhida = sessoes[escolha]
        nome = input("\nNome: ")
        try:
            nif = input("NIF: ")
            ingressoscomprados = int(input("Quantidade de ingressos a comprar: "))
        except ValueError:
            print("NIF e quantidade devem ser números.")
            return

        if sessao_escolhida['assentos_disponiveis'] >= ingressoscomprados:
            # Inserir cliente
            sql_cliente = """
                INSERT INTO cliente (nome, NIF, ingressos_comprados, sessao_id)
                VALUES (%s, %s, %s, %s)
            """
            valores_cliente = (nome, nif, ingressoscomprados, sessao_escolhida['id'])
            cursor.execute(sql_cliente, valores_cliente)

            # Atualizar assentos da sessão
            sql_update = """
                UPDATE sessao
                SET assentos_disponiveis = assentos_disponiveis - %s
                WHERE id = %s
            """
            cursor.execute(sql_update, (ingressoscomprados, sessao_escolhida['id']))

            db.commit()
            print("Compra realizada com sucesso!")

        else:
            print("Não há ingressos suficientes.")

    except mysql.connector.Error as err:
        print(f"Erro no banco de dados: {err}")
    finally:
        cursor.close()
        db.close()

def delete():
    
    db = start_connection()
    cursor = db.cursor(dictionary=True)

    # Obter sessões do banco
    cursor.execute("SELECT * FROM sessao")
    sessoes = cursor.fetchall()

    if not sessoes:
        print("Nenhuma sessão cadastrada.")
        return

    print("\nSessões disponíveis:")
    for i, sessao in enumerate(sessoes):
        print(f"{i + 1} - {sessao['filme']} às {sessao['horario']} (ID: {sessao['id']})")

    id = int(input("Qual o id da sessão que deseja deletar?"))

    ids_validos = [s['id'] for s in sessoes]
    if id not in ids_validos:
        print("ID de sessão inválido.")
        return

    sql = "DELETE FROM sessao WHERE id = %s"

    cursor.execute(sql,(id,))
    db.commit()

    print("Sessão deletada com sucesso.")
    cursor.close()
    db.close()
    
print(mycursor.rowcount, "record(s) deleted")
def Menu():
    op=int(input("\n\n\n1-Adicionar filmes e sessões novas\n2-Listar sessões disponíveis" \
    "\n3-Comprar ingresso para uma sessão\n4-Mostrar ingressos de um cliente\n5-Remover sessão\nAguardando: "))
    if op==1:
        AddFilmes()
        op=int(input("1 - Voltar ao Menu | 0 - Encerrar o programa\nAguardando: "))
        if op==1:
            Menu()
        else:
            print("Encerrando...")

    if op==2:
        Sessao.ExibirSessao()

        op=input("1 - Voltar ao Menu | 0 - Encerrar o programa\nAguardando: ")
        if op=="1":
            Menu()
        else:
            print("Encerrando...")

    if op==3:
        ComprarIngressos()
        Menu()

    if op==4:
        Cliente.ExibirCliente()

        op=input("1 - Voltar ao Menu | 0 - Encerrar o programa\nAguardando: ")
        if op=="1":
            Menu()
        else:
            print("Encerrando...")
    
    if op==5:
        delete()
        Menu()
print("\n\n\n\nBEM VINDO AO CINEMA ACT\n(Escolha uma das opções do menu a seguir)\n-----------------------------------------------")           
Menu()