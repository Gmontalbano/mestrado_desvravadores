"""import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

links = ['ADRA',
         'Artes_e_Habilidades_Manuais',
         'Atividades_Agrícolas',
         'Atividades_Missionárias_e_Comunitárias',
         'Atividades_Profissionais',
         'Atividades_Recreativas',
         'Ciência_e_Saúde',
         'Estudos_da_Natureza',
         'Habilidades_Domésticas',
         ]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

for link in links:
    url = f'https://mda.wiki.br/{link}/'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        figcaptions = soup.find_all('figcaption')
        codes = [figcaption.find('b').text for figcaption in figcaptions]
        codes = [item for index, item in enumerate(codes) if item not in codes[:index]]
        print(codes)
        names = [figcaption.find('a').text for figcaption in figcaptions]
        names = [item for index, item in enumerate(names) if item not in names[:index]]
        print(names)
        for codigo, nome in zip(codes, names):
            print(codigo)
            print(nome)
            cursor.execute("INSERT INTO especialidades (codigo, nome) VALUES (?, ?)", (codigo, nome))

    else:
        print('Sem sucesso:', response.status_code)


# Faça um commit para salvar as alterações no banco de dados
conn.commit()

# Feche a conexão
conn.close()"""