import streamlit as st
from pgs.mestrados import get_mestrados
from PIL import Image
from utils.sql import get_mestrado_code,get_especialidades_list,insert_data_e,get_e_user,get_info_especialidades




def get_info(option, data):
    for item in data:
        if item[1] == option:
            return item
    return None


def calculardo_mestrado():
    especialidades_list = get_especialidades_list()
    choice  = st.selectbox("Adicione uma especialidade:", [op[1] for op in especialidades_list])
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
        if len(st.session_state.user_especialidades) == 0:
            st.session_state.user_especialidades = get_e_user()
            for x in st.session_state.user_especialidades:
                name = get_info_especialidades(x)
                mestrado_code = get_mestrado_code(x)
                if len(mestrado_code) > 0:
                    for c in mestrado_code:
                        cross_info[c[0]]['have'] += 1
                        cross_info[c[0]]['list'].append(name)
        else:
            for e in st.session_state.user_especialidades:
                info = get_info(e, especialidades_list)
                insert_data_e(u_code=1, e_code=info[0])
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

