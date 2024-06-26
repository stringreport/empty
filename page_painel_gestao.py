import pandas as pd
import streamlit as st
from tratamentos import tabela_conciliacao_nfs, group_status_empresa_pago, group_status_empresa_previsto, group_status_empresa_atrasado, group_status_empresa_pago_terceiro, group_status_empresa_previsto_terceiro, group_status_empresa_atrasado_terceiro, hist_montante, pGestao_datasets, list_year_hist_montante, list_month_hist_montante
from datetime import datetime
import plotly.express as px

st.set_page_config(layout="wide")

# GERAÇÃO DE INFORMAÇÕES -------------------------------------------------------------------

# Data Set contem:
# Coluna 1 a 4 - Historico do montante
# Coluna 5 a 8 - Histrico Estoque 
# Coluna 9 a 13 - Historico Contas a receber
# Coluna 14 a 18 - Historico pagamento

giro_corrente = 10
# PAGINA ------------------------------------------------------------------------------------

# Titulo da pagina
st.title('Painel de Controle')

st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)

colHead1, colHead2 = st.columns(2)

colHead1.markdown('Giro Disponivel')
colHead2.markdown(f"<p style='text-align: left; margin-top: -30px; font-size: 70px'>R$ {giro_corrente}</p>", unsafe_allow_html=True)


# DIV 2:3 -RELAÇÃOD E PAINEIS

pan1, pan2, pan3 = st.columns(3)

list_year_brain = [2024,2025,2026,2027,2020,2029,2030]
list_month_brain = [1,2,3,4,5,6,7,8,9,10]


pan1.markdown(f"<h4 style='text-align: left;'>Brain</h4>", unsafe_allow_html=True)
brain_year = pan3.selectbox('Ano',list_year_brain)
brain_month = pan2.selectbox('Mês',list_month_brain)

ppan1, ppan2, ppan3 = st.columns(3)

# GRAFICO DO MONTANTE
brain_frame_montante = pGestao_datasets[(pGestao_datasets['ANO MONTANTE'] == brain_year) & (pGestao_datasets['MES MONTANTE'] == brain_month) ]
brain_frame_montante['DATA'] = brain_frame_montante['DATA'].astype(str)
brain_graph_montante =px.area(brain_frame_montante,x='DATA',y='GIRO',title='Montante',color_discrete_sequence=['#836FFF'])
brain_graph_montante.update_layout(xaxis_title=None, yaxis_title=None)
ppan1.plotly_chart(brain_graph_montante)

# GRAFICO A RECEBER PREVISTO
brain_frame_mreceber_previsto = pGestao_datasets[(pGestao_datasets['ANO RECEBER'] == brain_year) & (pGestao_datasets['MES RECEBER'] == brain_month) ]
brain_frame_mreceber_previsto['DATA.2'] = brain_frame_mreceber_previsto['DATA.2'].astype(str)
brain_graph_receber_previsto =px.area(brain_frame_mreceber_previsto,x='DATA.2',y='PREVISTO',title='A receber - Previsto',color_discrete_sequence=['#00FF7F'])
brain_graph_receber_previsto.update_layout(xaxis_title=None, yaxis_title=None)
ppan2.plotly_chart(brain_graph_receber_previsto)

# GRAFICO A RECEBER ATRASADO
brain_frame_receber_atrasado = pGestao_datasets[(pGestao_datasets['ANO RECEBER'] == brain_year) & (pGestao_datasets['MES RECEBER'] == brain_month) ]
brain_frame_receber_atrasado['DATA.2'] = brain_frame_receber_atrasado['DATA.2'].astype(str)
brain_graph_receber_atrasado =px.area(brain_frame_receber_atrasado,x='DATA.2',y='ATRASADO',title='A receber - Atrasado',color_discrete_sequence=['#00FF7F'])
brain_graph_receber_atrasado.update_layout(xaxis_title=None, yaxis_title=None)
ppan3.plotly_chart(brain_graph_receber_atrasado)

# GRAFICO A PAGAR - ATRASADO
brain_frame_pagar_atrasado = pGestao_datasets[(pGestao_datasets['ANO PAGAR'] == brain_year) & (pGestao_datasets['MES PAGAR'] == brain_month) ]
brain_frame_pagar_atrasado['DATA.3'] = brain_frame_pagar_atrasado['DATA.3'].astype(str)
brain_graph_pagar_atrasado = px.area(brain_frame_pagar_atrasado,x='DATA.3',y='ATRASADO.1',title='A pagar - Atrasado',color_discrete_sequence=['#DC143C'])
brain_graph_pagar_atrasado.update_layout(xaxis_title=None, yaxis_title=None)
ppan1.plotly_chart(brain_graph_pagar_atrasado)

# GRAFICO A PAGAR - PREVISTO
brain_frame_pagar_previsto = pGestao_datasets[(pGestao_datasets['ANO PAGAR'] == brain_year) & (pGestao_datasets['MES PAGAR'] == brain_month) ]
brain_frame_pagar_previsto['DATA.3'] = brain_frame_pagar_previsto['DATA.3'].astype(str)
brain_graph_pagar_previsto = px.area(brain_frame_pagar_previsto,x='DATA.3',y='PREVISTO.1',title='A pagar - Previsto',color_discrete_sequence=['#DC143C'])
brain_graph_pagar_previsto.update_layout(xaxis_title=None, yaxis_title=None)
ppan2.plotly_chart(brain_graph_pagar_previsto)

# GRAFICO AESTOQUE
brain_frame_estoque = pGestao_datasets[(pGestao_datasets['ANO ESTOQUE'] == brain_year) & (pGestao_datasets['MES ESTOQUE'] == brain_month) ]
brain_frame_estoque['DATA.1'] = brain_frame_estoque['DATA.1'].astype(str)
brain_graph_estoque =px.area(brain_frame_estoque,x='DATA.1',y='VALOR',title='Estoque',color_discrete_sequence=['#00FF7F'])
brain_graph_estoque.update_layout(xaxis_title=None, yaxis_title=None)
ppan3.plotly_chart(brain_graph_estoque)





st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)




# DIV 2 - 3
st.markdown(f"<h4 style='text-align: left;'>Recebimentos</h4>", unsafe_allow_html=True)
colStatus1, colStatus2, colStatus3 = st.columns(3)

# VALOR PAGO
colStatus1.markdown(f"<h6 style='text-align: center;'>PAGO</h6>", unsafe_allow_html=True)
colStatus1.dataframe(group_status_empresa_pago, use_container_width=True)
total_pago_receber = "{:,.2f}".format(pd.DataFrame(group_status_empresa_pago)['VALOR'].sum()).replace('.', '#').replace(',', '.').replace('#', ',')
colStatus1.markdown(f"<h6 style='text-align: right; margin-top: -10px;'>Total: R$ {total_pago_receber}</h6>", unsafe_allow_html=True)

# VALOR PREVISTO
colStatus2.markdown(f"<h6 style='text-align: center;'>PREVISTO</h6>", unsafe_allow_html=True)
colStatus2.dataframe(group_status_empresa_previsto, use_container_width=True)
total_previsto_receber = "{:,.2f}".format(pd.DataFrame(group_status_empresa_previsto)['VALOR'].sum()).replace('.', '#').replace(',', '.').replace('#', ',')
colStatus2.markdown(f"<h6 style='text-align: right; margin-top: -10px;'>Total: R$ {total_previsto_receber}</h6>", unsafe_allow_html=True)

# VALOR ATRASADO
colStatus3.markdown(f"<h6 style='text-align: center;'>ATRASADO</h6>", unsafe_allow_html=True)
colStatus3.dataframe(group_status_empresa_atrasado, use_container_width=True)
total_atrasado_receber = "{:,.2f}".format(pd.DataFrame(group_status_empresa_atrasado)['VALOR'].sum()).replace('.', '#').replace(',', '.').replace('#', ',')
colStatus3.markdown(f"<h6 style='text-align: right; margin-top: -10px;'>Total: R$ {total_atrasado_receber}</h6>", unsafe_allow_html=True)

st.write('')
# DIV 3 - 3
colStatusTerceiro1, colStatusTerceiro2, colStatusTerceiro3 = st.columns(3)

# VALOR PAGO
colStatusTerceiro1.markdown(f"<h6 style='text-align: center;'>PAGO - TERCEIROS</h6>", unsafe_allow_html=True)
colStatusTerceiro1.dataframe(group_status_empresa_pago_terceiro, use_container_width=True)
total_pago_receber_terceiro = "{:,.2f}".format(pd.DataFrame(group_status_empresa_pago_terceiro)['VALOR'].sum()).replace('.', '#').replace(',', '.').replace('#', ',')
colStatusTerceiro1.markdown(f"<h6 style='text-align: right; margin-top: -10px;'>Total: R$ {total_pago_receber_terceiro}</h6>", unsafe_allow_html=True)

# VALOR PREVISTO
colStatusTerceiro2.markdown(f"<h6 style='text-align: center;'>PREVISTO - TERCEIROS</h6>", unsafe_allow_html=True)
colStatusTerceiro2.dataframe(group_status_empresa_previsto_terceiro, use_container_width=True)
total_previsto_receber_terceiro = "{:,.2f}".format(pd.DataFrame(group_status_empresa_previsto_terceiro)['VALOR'].sum()).replace('.', '#').replace(',', '.').replace('#', ',')
colStatusTerceiro2.markdown(f"<h6 style='text-align: right; margin-top: -10px;'>Total: R$ {total_previsto_receber_terceiro}</h6>", unsafe_allow_html=True)

# VALOR ATRASADO
colStatusTerceiro3.markdown(f"<h6 style='text-align: center;'>ATRASADO - TERCEIROS</h6>", unsafe_allow_html=True)
colStatusTerceiro3.dataframe(group_status_empresa_atrasado_terceiro, use_container_width=True)
total_atrasado_receber_terceiro = "{:,.2f}".format(pd.DataFrame(group_status_empresa_atrasado_terceiro)['VALOR'].sum()).replace('.', '#').replace(',', '.').replace('#', ',')
colStatusTerceiro3.markdown(f"<h6 style='text-align: right; margin-top: -10px;'>Total: R$ {total_atrasado_receber_terceiro}</h6>", unsafe_allow_html=True)

# DIV HOSTORICOS ----------------------------------------------------------------------

st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: left;'>Históricos</h4>", unsafe_allow_html=True)

# DIV 4 - 2
colHist1, colHist2 = st.columns(2)

list_type_historicos=['MONTANTE','ESTOQUE','A RECEBER - ATRASADO','A RECEBER - PREVISTO','A PAGAR - ATRASADO','A PAGAR - PREVISTO']

input_historico = colHist1.selectbox('Histórico',list_type_historicos) # Escolher relatoio
input_year_hist = colHist1.selectbox('Ano',list_year_hist_montante) 
input_month_hist = colHist1.selectbox('Mês',list_month_hist_montante) 

if input_historico == 'MONTANTE':
    filtered_hist_montante = pGestao_datasets[(pGestao_datasets['ANO MONTANTE'] == input_year_hist) & (pGestao_datasets['MES MONTANTE'] == input_month_hist) ]
    filtered_hist_montante['DATA'] = filtered_hist_montante['DATA'].astype(str)
    colHist2.dataframe(filtered_hist_montante[['DATA','GIRO']], use_container_width=True, height=665)
    graph_montante =px.area(filtered_hist_montante,x='DATA',y='GIRO',title='Montante por Dia',color_discrete_sequence=['#4F4F4F'])
    colHist1.plotly_chart(graph_montante)

