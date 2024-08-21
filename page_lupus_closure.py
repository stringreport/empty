import pandas as pd
import streamlit as st
from tratamentos import tabela_extratolupus

def format_number(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Configurações da pagina
st.set_page_config(layout="wide")

st.title('FECHAMENTO LUPUS')
st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)

initial_date_c, final_date_c = st.columns(2)

initial_date = initial_date_c.date_input('Data Inicial')
final_date = final_date_c.date_input('Data Final')

filtered_frame = tabela_extratolupus.copy()
filtered_frame_previous_value =  filtered_frame[filtered_frame['DATA'] < initial_date]
previous_line = filtered_frame_previous_value['SALDO'].tail(1).values[0]
previous_line_float = float(previous_line.replace('.','').replace(',','.'))

#COLUNAS (Divs) PRIMARIAS -------------------------------
p1, p2, p3 = st.columns(3)

st.markdown("</br>",unsafe_allow_html=True)
st.markdown("</br>",unsafe_allow_html=True)
st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)
st.markdown(f"<h7 style='text-align: center;'>Detalhado</h7>", unsafe_allow_html=True)

# PAGAMENTO LUPUS --------------------------------------------------------------

filtered_frame_paglupus = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'PAGAMENTO LUPUS') &
(filtered_frame['DATA'] != '') ]
hf_pglupus = (35 * len(filtered_frame_paglupus) ) + 36
total_paglupus = filtered_frame_paglupus['VALOR'].sum()
filtered_frame_paglupus = filtered_frame_paglupus.drop(columns='SALDO')

if filtered_frame_paglupus.empty == False:
    a1, a2 = st.columns(2)
    a1.markdown(f"<h6 style='text-align: left; color: blue;'>PAGAMENTOS XGO</h6>", unsafe_allow_html=True)
    a2.markdown(f"<h6 style='text-align: right;'>{total_paglupus:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_paglupus, use_container_width=True, height=hf_pglupus)
else:
    pass

# DESCONTOS --------------------------------------------------------------

filtered_frame_desconto = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'DESCONTOS') &
(filtered_frame['DATA'] != '') ]
filtered_frame_desconto = filtered_frame_desconto.drop(columns='SALDO')
hf_desconto = (35 * len(filtered_frame_desconto) ) + 36
total_desconto = filtered_frame_desconto['VALOR'].sum()

if filtered_frame_desconto.empty == False:
    a3, a4 = st.columns(2)
    a3.markdown(f"<h6 style='text-align: left; color: red;'>DESCONTOS ADICIONADOS</h6>", unsafe_allow_html=True)
    a4.markdown(f"<h6 style='text-align: right;'>{total_desconto:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_desconto, use_container_width=True, height=hf_desconto)
else:
    pass

# ACERTOS --------------------------------------------------------------

filtered_frame_acerto = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'ACERTOS') &
(filtered_frame['DATA'] != '') ]
hf_acerto = (35 * len(filtered_frame_acerto) ) + 36
total_acerto = filtered_frame_acerto['VALOR'].sum()
filtered_frame_acerto = filtered_frame_acerto.drop(columns='SALDO')

if filtered_frame_acerto.empty == False:
    a5, a6 = st.columns(2)
    a5.markdown(f"<h6 style='text-align: left; color: blue;'>ACORDOS</h6>", unsafe_allow_html=True)
    a6.markdown(f"<h6 style='text-align: right;'>{total_acerto:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_acerto, use_container_width=True, height=hf_acerto)
else:
    pass

# REPASSE --------------------------------------------------------------

filtered_frame_repasse = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'REPASSE') &
(filtered_frame['DATA'] != '') ]
hf_repasse = (35 * len(filtered_frame_repasse) ) + 36
total_repasse = filtered_frame_repasse['VALOR'].sum()
filtered_frame_repasse = filtered_frame_repasse.drop(columns='SALDO')

if filtered_frame_repasse.empty == False:
    a7, a8 = st.columns(2)
    a7.markdown(f"<h6 style='text-align: left; color: blue;'>REPASSE 5%</h6>", unsafe_allow_html=True)
    a8.markdown(f"<h6 style='text-align: right;'>{total_repasse:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_repasse, use_container_width=True, height=hf_repasse)
else:
    pass

# CARREGADO FABRICA MG --------------------------------------------------------------

filtered_frame_fabricamg = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'CARREGADO FABRICA - MG') &
(filtered_frame['DATA'] != '') ]
hf_fabricamg = (35 * len(filtered_frame_fabricamg) ) + 36
total_fabricamg = filtered_frame_fabricamg['VALOR'].sum()
filtered_frame_fabricamg = filtered_frame_fabricamg.drop(columns='SALDO')

if filtered_frame_fabricamg.empty == False:
    a9, a10 = st.columns(2)
    a9.markdown(f"<h6 style='text-align: left; color: red;'>CARREGADO - MINAS GERAIS</h6>", unsafe_allow_html=True)
    a10.markdown(f"<h6 style='text-align: right;'>{total_fabricamg:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_fabricamg, use_container_width=True, height=hf_fabricamg)
else:
    pass

# CARREGADO FABRICA RJ --------------------------------------------------------------

filtered_frame_fabricarj = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'CARREGADO FABRICA - RJ') ]
hf_fabricarj = (35 * len(filtered_frame_fabricarj)) + 36
total_fabricarj = filtered_frame_fabricarj['VALOR'].sum()
filtered_frame_fabricarj = filtered_frame_fabricarj.drop(columns='SALDO')

if filtered_frame_fabricarj.empty == False:
    a11, a12 = st.columns(2)
    a11.markdown(f"<h6 style='text-align: left; color: red;'>CARREGADO - RIO DE JANEIRO</h6>", unsafe_allow_html=True)
    a12.markdown(f"<h6 style='text-align: right;'>{total_fabricarj:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_fabricarj, use_container_width=True, height=hf_fabricarj)
else:
    pass

# MATERIA PRIMA MG --------------------------------------------------------------

filtered_frame_farelomg = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'MATERIA PRIMA - MG') &
(filtered_frame['DATA'] != '') ]
hf_farelomg = (35 * len(filtered_frame_farelomg) ) + 36
total_farelomg = filtered_frame_farelomg['VALOR'].sum()
filtered_frame_farelomg = filtered_frame_farelomg.drop(columns='SALDO')

if filtered_frame_farelomg.empty == False:
    a13, a14 = st.columns(2)
    a13.markdown(f"<h6 style='text-align: left; color: blue;'>MATERIA PRIMA - MINAS GERAIS</h6>", unsafe_allow_html=True)
    a14.markdown(f"<h6 style='text-align: right;'>{total_farelomg:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_farelomg, use_container_width=True, height=hf_farelomg)
else:
    pass

# MATERIA PRIMA RJ --------------------------------------------------------------

filtered_frame_farelorj = filtered_frame[(filtered_frame['DATA'] >= initial_date) &
(filtered_frame['DATA'] <= final_date) &
(filtered_frame['REFERENCIA'] == 'MATERIA PRIMA - RJ') &
(filtered_frame['DATA'] != '') ]
hf_farelorj = (35 * len(filtered_frame_farelorj) ) + 36
total_farelorj = filtered_frame_farelorj['VALOR'].sum()
filtered_frame_farelorj = filtered_frame_farelorj.drop(columns='SALDO')

if filtered_frame_farelorj.empty == False:
    a15, a16 = st.columns(2)
    a15.markdown(f"<h6 style='text-align: left; color: blue'>MATERIA PRIMA - RIO DE JANEIRO</h6>", unsafe_allow_html=True)
    a16.markdown(f"<h6 style='text-align: right;'>{total_farelorj:.2f}</h6>", unsafe_allow_html=True)
    st.dataframe(filtered_frame_farelorj, use_container_width=True, height=hf_farelorj)
else:
    pass

# VALIDAÇAO DAS VARIAAVEIS (Coluna VALOR) SE EXISTENTES

# Frame cabeçalho
frame_summary_closure_add = pd.DataFrame({ 
    'ITEM' : ['ACERTOS','MATERIA PRIMA MG','MATERIA PRIMA RJ','PAGAMENTOS XGO','REPASSE 5%'],
    'VALOR' : [total_acerto,total_farelomg,total_farelorj,total_paglupus,total_repasse]
})

frame_summary_closure_sub = pd.DataFrame({ 
    'ITEM' : ['CARREGADO MG','CARREGADO RJ','DESCONTOS'],
    'VALOR' : [total_fabricamg,total_fabricarj,total_desconto]
})

frame_summary_closure_add.reset_index(drop=True, inplace=True)
p1.dataframe(frame_summary_closure_add, use_container_width=True)

frame_summary_closure_sub.reset_index(drop=True, inplace=True)
p2.dataframe(frame_summary_closure_sub, use_container_width=True)

total_add = frame_summary_closure_add['VALOR'].sum() - total_paglupus
total_sub = frame_summary_closure_sub['VALOR'].sum()
balance = total_add + total_sub + total_paglupus + previous_line_float
previous_balance = previous_line_float + total_paglupus
week_closure = total_add + total_sub

total_add = format_number(total_add)
total_sub = format_number(total_sub)
total_paglupus_f = format_number(total_paglupus)
balance = format_number(balance)
previous_balance_f = format_number(previous_balance)
week_closure_f = format_number(week_closure)

p3.markdown(f"<h6 style='text-align: right;'>Fechado semana anterior: {previous_line}</h6>", unsafe_allow_html=True)
p3.markdown(f"<h6 style='text-align: right;'>Foi pago: {total_paglupus_f}</h6>", unsafe_allow_html=True)
p3.markdown(f"<h6 style='text-align: right;'>Ficou em aberto: {previous_balance_f}</h6>", unsafe_allow_html=True)
p3.markdown(f"</br>", unsafe_allow_html=True)
p3.markdown(f"<h6 style='text-align: right; color: blue;'>A receber: {total_add}</h6>", unsafe_allow_html=True)
p3.markdown(f"<h6 style='text-align: right; color: red;'>A pagar: {total_sub}</h6>", unsafe_allow_html=True)
p3.markdown(f"<h6 style='text-align: right;'>Fechamento da Semana: {week_closure_f}</h6>", unsafe_allow_html=True)
p3.markdown(f"<h5 style='text-align: right;'>Saldo atual: {balance}</h5>", unsafe_allow_html=True)


