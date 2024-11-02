import pandas as pd
import streamlit as st
from pptx import Presentation
from utils.ppt import duplicate_slides, replace_text
import io


def make():
    uploaded_file = st.file_uploader("Faça o upload de um arquivo XLSX com os dados dos usuários", type=["xlsx"])
    ppt = st.file_uploader("Faça o upload de um arquivo ppt modelo", type=["pptx"])


    qtd = st.number_input("Quantas etiquetas temos por página", step=1)
    qtd = int(qtd)
    if st.button('Gerar'):
        pptx = Presentation(ppt)
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        linhas = len(df)
        copias = linhas // qtd
        print(copias)
        if linhas % qtd != 0:
            copias += 1

        print(f"Duplicando o slide {copias - 1} vezes")
        # ppt = duplicate_slides(pptx, n_copies=copias - 1)

        keys = []
        words = []
        colunas = df.columns.tolist()
        for c in colunas:
            for index, row in df.iterrows():
                keys.append(f'{c}')
                words.append(row[c])

        for search_string, replace_string in zip(keys, words):
            ppt = replace_text(ppt, search_string, replace_string, how='first')
        # ppt.save('etiquetas_finalizado.pptx')

        towrite = io.BytesIO()
        ppt.save(towrite)

        st.download_button(label='Download pptx',
                           data=towrite,
                           file_name='etiquetas.pptx')
        print(keys)
        print(words)