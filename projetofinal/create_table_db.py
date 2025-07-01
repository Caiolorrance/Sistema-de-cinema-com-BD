from connect_db import start_connection


mydb = start_connection()

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS filmes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), duração VARCHAR(255), classificação VARCHAR(255), indicativa VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS sessao (id INT AUTO_INCREMENT PRIMARY KEY, filme VARCHAR(255), horario VARCHAR(255), assentos_disponiveis INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS cliente (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), NIF VARCHAR(255), ingressos_comprados VARCHAR(255), sessao_id INT)")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)