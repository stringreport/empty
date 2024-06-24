import pandas as pd
import streamlit as st
from tratamentos import tabela_conciliacao_nfs
from datetime import datetime

st.set_page_config(layout="wide")

# Titulo da pagina
st.title('Relatórios - Planilha Carregamentos')

# Lista de opções de relatorios
list_report_options = ['PEDIDOS PENDENTES', 'COMPRA LUPUS', 'REPASSE LUPUS', 'REPASSE MARCIO MALTA']

input_report = st.selectbox('Selecione o relaório',list_report_options) # Escolher relatoio
st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)

if input_report == 'PEDIDOS PENDENTES':

    # Filtrando a tabela com os dados a ser trabalhados
    tabela_conciliacao_nfs = tabela_conciliacao_nfs[['CLIENTE','PEDIDO CLIENTE','DESTINO','PESO VENDA','STATUS']]
    tabela_conciliacao_nfs = tabela_conciliacao_nfs[(tabela_conciliacao_nfs['STATUS'] == ' PREVISTO ') | (tabela_conciliacao_nfs['STATUS'] == ' EM ROTA ') | (tabela_conciliacao_nfs['STATUS'] == ' CARREGADO ')  ]

    # Fzendo as contagens separadas por Status
    count_previsto = tabela_conciliacao_nfs[tabela_conciliacao_nfs['STATUS'] == ' PREVISTO ']
    count_emrota = tabela_conciliacao_nfs[tabela_conciliacao_nfs['STATUS'] == ' EM ROTA '] 
    count_carregado = tabela_conciliacao_nfs[tabela_conciliacao_nfs['STATUS'] == ' CARREGADO ']
    total_open_orders = count_previsto["STATUS"].count() + count_emrota["STATUS"].count() + count_carregado["STATUS"].count() # Soma dos 3 status

    st.markdown("<h6 style='text-align: left;'>Clientes que faltam entregar os pedidos</h6>", unsafe_allow_html=True)

    col_data1, col_data2 = st.columns(2) # Declarando a abertura de 2 DIVS

    # Agrupamento de clientes com pedidos abertos
    group_clients = tabela_conciliacao_nfs.groupby('CLIENTE')['PEDIDO CLIENTE'].count()
    col_data1.dataframe(group_clients, width=500) # Inseindo na div1

    # Adicionando 2 DIVs na coluna 2 criada acima
    subcol_data2_1, subcol_data2_2 = col_data2.columns(2)

    # Adicionando na subcoluna 1 da DIV 2 - Contagem de Agrupamento por Status
    group_status = tabela_conciliacao_nfs.groupby('STATUS')['STATUS'].count()
    subcol_data2_1.dataframe(group_status, width=250)

    # DIV para mostrar o total de pedidos em aberto - Sera adiconada na subcona 2 da DIV 2
    div_total_order = """
    <div style="background-color: #F4D03F; padding-top: 5px; border-radius: 20px;">
        <p style="font-size: 20px; text-align: center;">Pedidos em aberto:</p>
        <p style="font-size: 35px; text-align: center;">{}</p> 
    </div>
    """.format(total_open_orders)
    subcol_data2_2.markdown(div_total_order, unsafe_allow_html=True)



    st.markdown("<h5 style='text-align: left;'>Tabela</h5>", unsafe_allow_html=True)
    height_frame = 37 * len(tabela_conciliacao_nfs)
    st.dataframe(tabela_conciliacao_nfs, height=height_frame, width=1200)

if input_report == 'REPASSE LUPUS':

    # Definindo as colunas de datas e suas variaveis
    coldate_init, coldate_end = st.columns(2)
    init_date = coldate_init.date_input('Data inicial')
    end_date = coldate_end.date_input('Data final')

    # Frame filtrado de acordo com as datas selecionada
    filtered_frame = tabela_conciliacao_nfs[(tabela_conciliacao_nfs['DATA EMISSAO'] >= init_date.strftime("%Y-%m-%d"))
    & (tabela_conciliacao_nfs['DATA EMISSAO'] <= end_date.strftime("%Y-%m-%d"))
    & (tabela_conciliacao_nfs['REPRESENTANTE'] == ' LUPUS ')
    ] # Filtros: Maior que data de Inicio, Menor que data de Fim, Representante igual a Lupus

    # Totais para o painel principal
    total_faturado = filtered_frame['LUPUS'].sum().round(2)
    total_repasse = total_faturado * 0.05
    qnt_nfs_periodo = filtered_frame['NF VENDA'].count()
    total_faturado_formatado = "{:,.2f}".format(total_faturado).replace('.', '#').replace(',', '.').replace('#', ',')
    total_repasse_formatado = "{:,.2f}".format(total_repasse).replace('.', '#').replace(',', '.').replace('#', ',')

    colvalue1, colvalue2 = st.columns(2)

    # TOTAL FATURADO
    colvalue1.write('')
    colvalue1.write('Total Faturado')
    colvalue1.markdown(f"<p style='text-align: left; margin-top: -30px; font-size: 70px'>R$ {total_faturado_formatado}</p>", unsafe_allow_html=True)

    # TOTAL REPASSE
    colvalue2.write('')
    colvalue2.write('Total Repasse')
    colvalue2.markdown(f"<p style='color: #00FF7F; text-align: left; margin-top: -30px; font-size: 70px';> R${total_repasse_formatado}</p>", unsafe_allow_html=True)

    # Criando coluna para calcular repasse de cada NF
    filtered_frame['REPASSE'] = filtered_frame['LUPUS'] * 0.05
    filtered_frame['REPASSE'] = filtered_frame['REPASSE'].round(2)

    # Transformando coluna de data em string para que o TIME nao apareça na coluna
    filtered_frame['DATA EMISSAO'] = filtered_frame['DATA EMISSAO'].astype(str)

    st.write('')
    height_frame = 35 * (len(filtered_frame) + 1)
    st.dataframe(filtered_frame[['DATA EMISSAO','NF VENDA','CLIENTE','LUPUS','REPASSE']], width=1200, height=height_frame) # teste






