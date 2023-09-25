import sqlite3
import streamlit as st
# Conecte-se ao seu banco de dados SQLite



def get_mestrado_code(code):
    conn = sqlite3.connect('./utils/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT mestrado_codigo FROM MestradoEspecialidade WHERE especialidade_codigo = ?", (code,))
    # Recuperar os resultados da consulta
    mestrados_code = cursor.fetchall()
    return mestrados_code
def get_especialidades_list():
    conn = sqlite3.connect('./utils/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM especialidades")
    # Recuperar os resultados da consulta
    especialidades_list = cursor.fetchall()
    return especialidades_list
def get_mestrados():
    conn = sqlite3.connect('./utils/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mestrados")
    # Recuperar os resultados da consulta
    mestrados_list = cursor.fetchall()
    return mestrados_list

def get_info_mestrados(codigo):
    conn = sqlite3.connect('./utils/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MestradoEspecialidade WHERE mestrado_codigo = ?", (codigo,))
    # Recuperar os resultados da consulta
    especialidades_list = cursor.fetchall()
    return especialidades_list
def get_info_especialidades(codigo):
    conn = sqlite3.connect('./utils/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM especialidades WHERE codigo = ?", (codigo,))
    nome = cursor.fetchall()
    return nome[0][0]