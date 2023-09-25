import streamlit as st
import sqlite3
from pgs.mestrados import get_mestrados
from PIL import Image

# Conecte-se ao seu banco de dados SQLite
conn = sqlite3.connect('./utils/data.db')
cursor = conn.cursor()
if "user_especialidades" not in st.session_state:
    st.session_state.user_especialidades = []

if "load_state" not in st.session_state:
    st.session_state.load_state = False


def get_info(option, data):
    for item in data:
        if item[1] == option:
            return item
    return None

def get_mestrado_code(code):
    cursor.execute("SELECT mestrado_codigo FROM MestradoEspecialidade WHERE especialidade_codigo = ?", (code,))
    # Recuperar os resultados da consulta
    mestrados_code = cursor.fetchall()

    return mestrados_code

def calculardo_mestrado():
    cursor.execute("SELECT * FROM especialidades")
    # Recuperar os resultados da consulta
    especialidades_list = cursor.fetchall()
    choice = st.selectbox("Adicione uma especialidade:", [op[1] for op in especialidades_list])
    if st.button("Adicionar"):
        if choice not in st.session_state.user_especialidades:
            st.session_state.user_especialidades.append(choice)
    for e in st.session_state.user_especialidades:
        st.write(e)
    if st.button("Calcular mestrados!") or st.session_state.load_state:
        st.session_state.load_state = True
        mestrados_list = get_mestrados()
        cross_info = {}
        for m in mestrados_list:
            cod = m[0]
            qtd = m[2]
            cross_info[cod] = {'cod': cod,
                               'min': qtd,
                               'have': 0,
                               'list': []}
        for e in st.session_state.user_especialidades:
            info = get_info(e, especialidades_list)
            mestrado_code = get_mestrado_code(info[0])
            if len(mestrado_code) > 0:
                for c in mestrado_code:
                    cross_info[c[0]]['have'] += 1
                    cross_info[c[0]]['list'].append(e)

        #st.write(cross_info)
        col1, col2, col3 = st.columns(3)
        c = [col1,col2,col3]
        i=0
        for key, value in cross_info.items():
            with c[i]:  # Coluna I
                image = Image.open(f'./imgs/{key}.png')

                # Exibir a imagem na coluna
                st.image(image)
                st.metric(label=key, value=value['min'], delta=value['have'])
                for especialide in value['list']:
                    st.write(especialide)
                i+=1
                if i>2:
                    i=0

