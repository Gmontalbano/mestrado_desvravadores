import streamlit as st
import sqlite3
from PIL import Image

# Conecte-se ao seu banco de dados SQLite
conn = sqlite3.connect('./utils/data.db')
cursor = conn.cursor()


def get_mestrados():
    cursor.execute("SELECT * FROM Mestrados")
    # Recuperar os resultados da consulta
    mestrados_list = cursor.fetchall()
    return mestrados_list


def get_info(option, data):
    for item in data:
        if item[1] == option:
            return item
    return None


def get_info_mestrados(codigo):
    cursor.execute("SELECT * FROM MestradoEspecialidade WHERE mestrado_codigo = ?", (codigo,))
    # Recuperar os resultados da consulta
    especialidades_list = cursor.fetchall()
    return especialidades_list

def get_info_especialidades(codigo):
    cursor.execute("SELECT nome FROM especialidades WHERE codigo = ?", (codigo,))
    nome = cursor.fetchall()
    return nome[0][0]

def show_mestrado():
    m = get_mestrados()
    choice = st.selectbox("Selecione uma opção", [op[1] for op in m])
    info = get_info(choice, m)
    img, title_text = st.columns([1, 2])
    image = Image.open(f'imgs/{info[0]}.png')
    img.image(image, caption=info[0])
    if info:
        st.write(f"Você precisa ter {info[2]} especialidades da seguinte lista:")
        especialidades = get_info_mestrados(info[0])
        for e in especialidades:
            nome = get_info_especialidades(e[1])
            st.write(f"{e[1]} - {nome}")
    else:
        st.write("Opção selecionada não encontrada.")
