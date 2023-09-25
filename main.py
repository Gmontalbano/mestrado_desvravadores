import streamlit as st
from PIL import Image
from pgs import mestrados,calculadora


def main():
    img, title_text = st.columns([1, 2])
    image = Image.open('imgs/pc_logo.jpg')
    img.image(image, caption='Mais que um clube, uma familia')
    title_text.title("Pioneiros da colina")
    menu = ['Mestrados', 'Calculadora de mestrados']
    choice = st.sidebar.selectbox("Selecione uma opção", menu)
    if choice == "Mestrados":
        mestrados.show_mestrado()
    elif choice == 'Calculadora de mestrados':
        calculadora.calculardo_mestrado()
if __name__ == '__main__':
    main()

