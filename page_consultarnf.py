import pandas as pd
import streamlit as st
from tratamentos import tabela_conciliacao_nfs
from datetime import datetime

st.set_page_config(layout="wide")

# Titulo da pagina
st.title('Consultar Notas Fiscais')

# - FORMULARIO ------------------------------------------------------------------------------------------------------

# Opções para seleção da lista de empresas - usado no input_empresa
empresas = list(tabela_conciliacao_nfs['FATURAMENTO'].unique())
del empresas[0]

input_empresa = st.selectbox('Empresa', empresas) # Perguntar ao usuario

# Opções para seleção da nf - usado no input_nf
temp_frame_nfs = tabela_conciliacao_nfs[tabela_conciliacao_nfs['FATURAMENTO'] == input_empresa]
notas_fiscais = list(temp_frame_nfs['NF VENDA'].unique())
input_nf = st.selectbox('NF-e', notas_fiscais) # Perguntar ao usuario

st.markdown('<hr style="border-top: 1px solid #0A0A2A">', unsafe_allow_html=True)
# ---------------------------------------------------------------------------------------------------

# FRAME FILTRADO PARA REALIZAR PROCV
filtered_frame = tabela_conciliacao_nfs[(tabela_conciliacao_nfs['FATURAMENTO'] == input_empresa) & (tabela_conciliacao_nfs['NF VENDA'] == input_nf)] 

if filtered_frame['STATUS'].iloc[0] == ' CANCELADO ':
    st.markdown("<p style='text-align: left; color: #FF0040'>* Nota Fiscal Cancelada</p>", unsafe_allow_html=True)

elif filtered_frame['STATUS'].iloc[0] == ' BONIFICACAO ':
    st.markdown("<p style='text-align: left; color: #FFFF00'>* Nota Fiscal de Bonificação</p>", unsafe_allow_html=True)

# PARTE 1 - DADOS DE CADASTRO ------------------------------------------------------------------------------------------

st.markdown("<h4 style='text-align: left;'>Cadastro</h4>", unsafe_allow_html=True)

# NOME DO CLIENTE
st.text_input('Cliente', value=filtered_frame['CLIENTE'].iloc[0])

col1, col2, col3 = st.columns(3)

# DATA DE EMISSAO
col1.text_input('Emissão', value=datetime.strptime(str(filtered_frame['DATA EMISSAO'].iloc[0]), "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y"))

# NUMERO DO PEDIDO
col2.text_input('Pedido',value=filtered_frame['NF REF'].iloc[0])

# REPRESENTANTE
col3.text_input('Representante',value=filtered_frame['REPRESENTANTE'].iloc[0])

# -----------------------------------------------------------------------------------------------------------------------

# PARTE 2 - DADOS FINANCEIROS -------------------------------------------------------------------------------------------

st.write('')
st.markdown("<h4 style='text-align: left;'>Financeiro</h4>", unsafe_allow_html=True)

# FATURAMENTO
st.text_input('Faturado', value=filtered_frame['VALOR VENDA'].iloc[0])

colf1, colf2, colf3 = st.columns(3)

# RETIRADO GALPAO
colf1.text_input('Retirado Galpão',value=filtered_frame['GALPAO'].iloc[0])

# RETIRADO PARANAFOODS
colf2.text_input('Retirado ParanaFoods',value=filtered_frame['  PARANA '].iloc[0])

# RETIRADO LUPUS
colf3.text_input('Retirado Lupus',value=filtered_frame['LUPUS'].iloc[0])
st.write('')

taxas1, taxas2 = st.columns(2)

# VALOR COMISSAO
taxas1.text_input('Comissão',value=filtered_frame['COMISSAO'].iloc[0])

# COMISSAO %
taxas2.text_input('Comissão %',value=filtered_frame['COMISSAO %'].iloc[0])

# VALOR ADMINISTRAÇÃO
taxas1.text_input('Custo Administração',value=filtered_frame['CUSTO ADM'].iloc[0])

# ADMINISTRAÇÃO %
taxas2.text_input('Custo Administração %',value=filtered_frame['CUSTO ADM %'].iloc[0])

# LUCRO BRUTO
taxas1.text_input('Lucro bruto',value=filtered_frame['LUCRO BRUTO'].iloc[0])

# LUCRO LIQUIDO
mask_lucro_liquido = f'{filtered_frame["LIQUIDO"].iloc[0]} ........... {filtered_frame[" % "].iloc[0]}%'
taxas2.text_input('Lucro liquido',value=mask_lucro_liquido)


# PARTE 3 - DADOS DE LOGISTICA -------------------------------------------------------------------------------------

st.write('')
st.markdown("<h4 style='text-align: left;'>Logística</h4>", unsafe_allow_html=True)

log1, log2 = st.columns(2)

# VOLUME DE ITENS
log1.text_input('Volume',value=filtered_frame['VOL VENDA'].iloc[0])

# PESO
log2.text_input('Peso',value=filtered_frame['PESO VENDA'].iloc[0])

# CIDADE
log1.text_input('Cidade',value=filtered_frame['DESTINO'].iloc[0])

# PESO
log2.text_input('Bairro',value=filtered_frame['BAIRRO'].iloc[0])


