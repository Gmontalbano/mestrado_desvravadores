import sqlite3

# Conectando ao banco de dados (ou criando um novo se ele não existir)
conexao = sqlite3.connect('data.db')

# Criando um cursor para interagir com o banco de dados
cursor = conexao.cursor()

cursor.execute('''
SELECT * FROM user_especialidades
''')

# Obtendo todos os resultados da consulta
resultados = cursor.fetchall()

# Exibindo os resultados
for linha in resultados:
    print(linha)

# Fechando a conexão
conexao.close()

from sql import get_e_user
get_e_user()