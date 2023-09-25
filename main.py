import streamlit as st
from PIL import Image
from pgs import mestrados,calculadora
import sqlite3
conn = sqlite3.connect('./utils/data.db')
cursor = conn.cursor()

def main():
    img, title_text = st.columns([1, 2])
    image = Image.open('imgs/pc_logo.jpg')
    img.image(image, caption='Mais que um clube, uma familia')
    title_text.title("Pioneiros da colina")
    menu = ['Mestrados', 'Calculadora de mestrados']
    choice = st.sidebar.selectbox("Selecione uma opção", menu)
    if choice == "Mestrados":
        mestrados.show_mestrado()
        conn.close()
    elif choice == 'Calculadora de mestrados':
        calculadora.calculardo_mestrado()
        conn.close()
if __name__ == '__main__':
    main()
    conn.close()
