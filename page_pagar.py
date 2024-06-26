import pandas as pd
import streamlit as st
from tratamentos import tabela_contas_pagar
from datetime import datetime

st.set_page_config(layout="wide")

# Titulo da pagina
st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)

# Lista de opções de relatorios
list_report_options = ['LISTA DE PAGAMENTOS']

input_report = st.selectbox('Selecione o relaório',list_report_options) # Escolher relatoio
st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)

if input_report == 'LISTA DE PAGAMENTOS':

    r1,r2,r3 = st.columns(3)
    r1.write('')
    limit_date = r2.date_input('Data Limite')
    r3.write('')
    st.write('')

    # Função para aplicar estilo condicional
    def style_status_cell(cell):
        """
        Função para aplicar estilo condicional na coluna 'STATUS'.
        """

        if cell == 'PREVISTO':
            return 'background-color: yellow; color: black;'

        if cell == 'ATRASADO':
            return 'background-color: red; color: white;'


    """ FRAME FILTRADO COM CONTAS DA TRANSPORTADORA  ------------------------------------------- """

    frame_transportadora = tabela_contas_pagar[(tabela_contas_pagar['MACRO EMPRESA'] == 'TRANSPORTADORA') & (tabela_contas_pagar['VENCIMENTO'] <= limit_date) & (tabela_contas_pagar['STATUS'] != 'PAGO') & (tabela_contas_pagar['STATUS'] != 'A PROGRAMAR')]
    frame_transportadora = frame_transportadora[['COMPETENCIA','VENCIMENTO',' VALOR ','STATUS','CATEGORIA','REFERENTE','MACRO EMPRESA']]
    height_frame_transportadora = 35 * (len(frame_transportadora) + 1)
    total_transportadora = "{:,.2f}".format(pd.DataFrame(frame_transportadora)[' VALOR '].sum()).replace('.', '#').replace(',', '.').replace('#', ',')

    trp1, trp2 = st.columns(2)
    trp1.markdown(f"<h4 style='text-align: left;'>Contas da Transportadora</h4>", unsafe_allow_html=True)
    trp2.markdown(f"<h4 style='text-align: right;'>R$ {total_transportadora}</h4>", unsafe_allow_html=True)
    st.dataframe(frame_transportadora.style.applymap(style_status_cell, subset=['STATUS']), use_container_width=True, height=height_frame_transportadora)


    """ FRAME FILTRADO COM CONTAS DA DISTRIBUIDORA  ------------------------------------------- """
    frame_distribuidora = tabela_contas_pagar[(tabela_contas_pagar['MACRO EMPRESA'] == 'DISTRIBUIDORA') & (tabela_contas_pagar['VENCIMENTO'] <= limit_date) & (tabela_contas_pagar['STATUS'] != 'PAGO') & (tabela_contas_pagar['STATUS'] != 'A PROGRAMAR')]
    frame_distribuidora = frame_distribuidora[['COMPETENCIA','VENCIMENTO',' VALOR ','STATUS','CATEGORIA','REFERENTE','MACRO EMPRESA']]
    height_frame_distribuidora = 35 * (len(frame_distribuidora) + 1)
    total_distribuidora = "{:,.2f}".format(pd.DataFrame(frame_distribuidora)[' VALOR '].sum()).replace('.', '#').replace(',', '.').replace('#', ',')

    st.write('')
    dst1, dst2 = st.columns(2)
    dst1.markdown(f"<h4 style='text-align: left;'>Contas da Distribuidora</h4>", unsafe_allow_html=True)
    dst2.markdown(f"<h4 style='text-align: right;'>R$ {total_distribuidora}</h4>", unsafe_allow_html=True)

    st.dataframe(frame_distribuidora.style.applymap(style_status_cell, subset=['STATUS']), use_container_width=True, height=height_frame_distribuidora)

    """ FRAME FILTRADO COM CONTAS DA MATERIA PRIMA  ------------------------------------------- """
    frame_materiaprima= tabela_contas_pagar[(tabela_contas_pagar['MACRO EMPRESA'] == 'MATERIA PRIMA') & (tabela_contas_pagar['VENCIMENTO'] <= limit_date) & (tabela_contas_pagar['STATUS'] != 'PAGO') & (tabela_contas_pagar['STATUS'] != 'A PROGRAMAR')]
    frame_materiaprima = frame_materiaprima[['COMPETENCIA','VENCIMENTO',' VALOR ','STATUS','CATEGORIA','REFERENTE','MACRO EMPRESA']]
    height_frame_materiaprima = 35 * (len(frame_materiaprima) + 1)
    total_materiaprima = "{:,.2f}".format(pd.DataFrame(frame_materiaprima)[' VALOR '].sum()).replace('.', '#').replace(',', '.').replace('#', ',')

    st.write('')
    mp1, mp2 = st.columns(2)
    mp1.markdown(f"<h4 style='text-align: left;'>Contas da Matéria Prima</h4>", unsafe_allow_html=True)
    mp2.markdown(f"<h4 style='text-align: right;'>R$ {total_materiaprima}</h4>", unsafe_allow_html=True)

    st.dataframe(frame_materiaprima.style.applymap(style_status_cell, subset=['STATUS']), use_container_width=True, height=height_frame_materiaprima)


# print(tabela_contas_pagar.head())




