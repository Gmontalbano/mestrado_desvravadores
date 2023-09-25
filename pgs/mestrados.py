import streamlit as st
from PIL import Image
from utils.sql import get_mestrados, get_info_mestrados, get_info_especialidades


def get_info(option, data):
    for item in data:
        if item[1] == option:
            return item
    return None


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
