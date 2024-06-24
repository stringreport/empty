
import pandas as pd
import streamlit as st
import plotly.express as px
from tratamentos import tabela_contas_pagar

tabela_contas_pagar = tabela_contas_pagar.sort_values('PAGAMENTO')

st.set_page_config(layout='wide') # Codigo para aproveitar todo o espaço da tela
box_month = st.sidebar.selectbox('MÊS', tabela_contas_pagar['DT VENCIMENTO'].unique())

tabela_contas_pagar['month_vencimento'] = tabela_contas_pagar['VENCIMENTO'].apply(lambda x: str(x.year) + '-' + str(x.month))
tabela_contas_pagar['month_competencia'] = tabela_contas_pagar['COMPETENCIA'].apply(lambda x: str(x.year) + '-' + str(x.month))
tabela_contas_pagar['month_pagamento'] = tabela_contas_pagar['PAGAMENTO'].apply(lambda x: str(x.year) + '-' + str(x.month))

filtered_frame = tabela_contas_pagar[tabela_contas_pagar['month_pagamento'] == box_month]
filtered_frame[['VENCIMENTO','PAGAMENTO','DOCUMENTO',' REFERENTE ',' VALOR ','CATEGORIA','CLASSIFICAÇÃO']]

# print(tabela_contas_pagar[['VENCIMENTO',' VALOR ']])



