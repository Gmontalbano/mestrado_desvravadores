'''import sqlite3

# Conecte-se ao seu banco de dados SQLite
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Consulta SQL para remover espaços da coluna especialidade_codigo
update_query = """
UPDATE MestradoEspecialidade
SET especialidade_codigo = 'AM-013'
WHERE especialidade_codigo LIKE 'AM-003' AND mestrado_codigo LIKE 'ME-001';
"""

try:
    # Execute a consulta de atualização
    cursor.execute(update_query)

    # Confirme as alterações
    conn.commit()
    print("Espaços removidos da coluna especialidade_codigo com sucesso.")

except Exception as e:
    # Em caso de erro, faça rollback das alterações
    conn.rollback()
    print("Erro ao remover espaços da coluna especialidade_codigo:", str(e))

finally:
    # Feche a conexão com o banco de dados
    conn.close()
'''