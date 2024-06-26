import pandas as pd 
# from page_painel_gestao import input_year_hist, input_month_hist

# CONTAS A PAGAR ------------------------------------------------------------------------------
tabela_contas_pagar = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSId0_Zh0fAmLE4ia9-t9UIpsZ98V-0Tqc0ba0E-zNAOnfOA195bLJ7pSHpYCiFe2NowTyZIJ1B5nFk/pub?gid=910529611&single=true&output=csv', header=1)
tabela_contas_pagar[' VALOR '] = tabela_contas_pagar[' VALOR '].str.replace('.','').str.replace(',','.').str.slice(3).astype(float)
tabela_contas_pagar[' REFERENTE '] = tabela_contas_pagar['REFERENTE'].astype(str)
# tabela_contas_pagar = tabela_contas_pagar[tabela_contas_pagar['DT PAGAMENTO'].notna() ]
tabela_contas_pagar['DT PAGAMENTO'] = tabela_contas_pagar['DT PAGAMENTO'].str.strip()
tabela_contas_pagar['CLASSIFICAÇÃO'] = tabela_contas_pagar['CLASSIFICAÇÃO'].str.strip()
tabela_contas_pagar['MACRO EMPRESA'] = tabela_contas_pagar['MACRO EMPRESA'].str.strip()
tabela_contas_pagar['CATEGORIA'] = tabela_contas_pagar['CATEGORIA'].str.strip()
tabela_contas_pagar['VENCIMENTO'] = pd.to_datetime(tabela_contas_pagar['VENCIMENTO'], format='%d/%m/%Y').dt.date
tabela_contas_pagar['COMPETENCIA'] = pd.to_datetime(tabela_contas_pagar['COMPETENCIA'], format='%d/%m/%Y').dt.date
tabela_contas_pagar['PAGAMENTO'] = pd.to_datetime(tabela_contas_pagar['PAGAMENTO'], format='%d/%m/%Y').dt.date
# ----------------------------------------------------------------------------------------------


# CONCILIAÇÃO DE NOTAS -------------------------------------------------------------------------
transform_columns = ['LUPUS','VALOR VENDA','LUCRO BRUTO','CUSTO ADM','COMISSAO','LIQUIDO',' % ']

tabela_conciliacao_nfs = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT4-fO1dCtnGNCaa2wK8ULj2Mgd5uKOPAUARs66Q4HpRQIQ0SSmXvSF0eOt-esIx_TBsMEWIHRUrcHI/pub?gid=1565722202&single=true&output=csv')
tabela_conciliacao_nfs['DATA EMISSAO'] = pd.to_datetime(tabela_conciliacao_nfs['DATA EMISSAO']  , format='%d/%m/%Y')
tabela_conciliacao_nfs['DATA EMISSAO'] = tabela_conciliacao_nfs['DATA EMISSAO'].dt.date
tabela_conciliacao_nfs[transform_columns] = tabela_conciliacao_nfs[transform_columns].apply(
    lambda col: col.str.replace('.','').str.replace(',','.').astype(float)
)
# ----------------------------------------------------------------------------------------------

# CPLANILHA GESTAO -------------------------------------------------------------------------

# EXTRAÇÃO DE DADOS DA PLANILHA GESWTAO - CENTRO DE DADOS
pGestao_datasets = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSd_0XR8nI68FKDUWTQDnUhs8cLxfhFsvQY-wS4u0DyReTvUjgZ95aWKEPzaJ8wvnNcQZgEs4UDJgiw/pub?gid=1201403855&single=true&output=csv', header=1)

# Tratamento de tipos de dados
list_data_transform = ['DATA','DATA.1','DATA.2','DATA.3'] # Colunas de datas 
i_date = 0
for i in list_data_transform:
  pGestao_datasets[list_data_transform[i_date]] = pd.to_datetime(pGestao_datasets[list_data_transform[i_date]], format='%d/%m/%Y')
  i_date = i_date + 1

list_float_transform = ['VALOR','PREVISTO','ATRASADO','PREVISTO.1','ATRASADO.1','GIRO'] # Colunas de numero real
i_float = 0
for i in list_float_transform:
  pGestao_datasets[list_float_transform[i_float]] = pGestao_datasets[list_float_transform[i_float]].str.replace('.','').str.replace(',','.').astype(float).round(2)
  i_float = i_float + 1

# Excluindo colunas inuteis
list_drop_columns = ['MES','ANO','MES.1','ANO.1','MES.2','ANO.2','MES.3','ANO.3']
pGestao_datasets = pGestao_datasets.drop(columns=list_drop_columns)

# Criando arrays necessários - Datas
pGestao_datasets['ANO MONTANTE'] = pGestao_datasets['DATA'].dt.year
pGestao_datasets['MES MONTANTE'] = pGestao_datasets['DATA'].dt.month
pGestao_datasets['ANO RECEBER'] = pGestao_datasets['DATA.2'].dt.year
pGestao_datasets['MES RECEBER'] = pGestao_datasets['DATA.2'].dt.month
pGestao_datasets['ANO PAGAR'] = pGestao_datasets['DATA.3'].dt.year
pGestao_datasets['MES PAGAR'] = pGestao_datasets['DATA.3'].dt.month
pGestao_datasets['ANO ESTOQUE'] = pGestao_datasets['DATA.1'].dt.year
pGestao_datasets['MES ESTOQUE'] = pGestao_datasets['DATA.1'].dt.month

# Historico do montante
hist_montante = pGestao_datasets[['DATA','GIRO']]
list_year_hist_montante = list(pGestao_datasets['ANO MONTANTE'].unique())
list_month_hist_montante = list(pGestao_datasets['MES MONTANTE'].unique())



hist_estoque = pGestao_datasets[['DATA.1','VALOR']]
hist_receber_previsto = pGestao_datasets[['DATA.2','PREVISTO']]
hist_receber_atrasado = pGestao_datasets[['DATA.2','ATRASADO']]
hist_pagar_previsto = pGestao_datasets[['DATA.3','PREVISTO.1']]
hist_pagar_previsto= pGestao_datasets[['DATA.3','ATRASADO.1']]
# ----------------------------------------------------------------------------------------------


# CONTAS A RECEBER -------------------------------------------------------------------------
# Dentro da planilha gestao

pGestao_receber = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSd_0XR8nI68FKDUWTQDnUhs8cLxfhFsvQY-wS4u0DyReTvUjgZ95aWKEPzaJ8wvnNcQZgEs4UDJgiw/pub?gid=350606272&single=true&output=csv')

# Excluindo colunas Inuteis
list_drop_columns_receber = ['Unnamed: 2','#VALUE!','DATA VEN.1','OBSERVAÇAO','DATA FAC','N BORDERO','RECOMPRA','EMPRESA FAC']
pGestao_receber = pGestao_receber.drop(columns=list_drop_columns_receber)

# Tratamento de tipos de dados
list_data_transform = ['EMISSÃO','DATA CANHOTO','DATA VEN','DATA RECEB'] # Colunas de datas
i_date = 0
for i in list_data_transform:
    pGestao_receber[list_data_transform[i_date]] = pd.to_datetime(pGestao_receber[list_data_transform[i_date]], format='mixed')
    i_date = i_date + 1

list_float_transform = ['VALOR','DESCONTO','PAGO','A RECEBER'] # Colunas de numero real
i_float = 0
for i in list_float_transform:
    pGestao_receber[list_float_transform[i_float]] = pGestao_receber[list_float_transform[i_float]].str.replace('.','').str.replace(',','.').astype(float).round(2)
    i_float = i_float + 1

list_strip_receber = ['REPRESENTANTE','STATUS','EMPRESA','CLIENTE','NF']
i_strip = 0
for i in list_strip_receber:
    pGestao_receber[list_strip_receber[i_strip]] = pGestao_receber[list_strip_receber[i_strip]].str.strip()
    i_strip = i_strip + 1

# PAGO POR EMPRESA
frame_receber_pago = pGestao_receber[(pGestao_receber['STATUS'] == 'PAGO') & (pGestao_receber['REPRESENTANTE'] != 'LUPUS') & (pGestao_receber['REPRESENTANTE'] != 'MG REPRESENTAÇÕES') ]
group_status_empresa_pago =  frame_receber_pago.groupby(['EMPRESA'])['VALOR'].sum()
# total_pago_empresa = group_status_empresa_pago['VALOR'].sum()

# A RECEBER POR EMPRESA
frame_receber_previsto = pGestao_receber[(pGestao_receber['STATUS'] == 'PREVISTO') & (pGestao_receber['REPRESENTANTE'] != 'LUPUS') & (pGestao_receber['REPRESENTANTE'] != 'MG REPRESENTAÇÕES') ]
group_status_empresa_previsto =  frame_receber_previsto.groupby(['EMPRESA'])['VALOR'].sum()

# ATRASADO POR EMPRESA
frame_receber_atrasado = pGestao_receber[(pGestao_receber['STATUS'] == 'ATRASADO') & (pGestao_receber['REPRESENTANTE'] != 'LUPUS') & (pGestao_receber['REPRESENTANTE'] != 'MG REPRESENTAÇÕES') ]
group_status_empresa_atrasado =  frame_receber_atrasado.groupby(['EMPRESA'])['VALOR'].sum()

# ------------------ TERCEIROS

# PAGO POR EMPRESA - TERCEIRO
frame_receber_pago_terceiro = pGestao_receber[(pGestao_receber['STATUS'] == 'PAGO') & (pGestao_receber['REPRESENTANTE'] == 'LUPUS') | (pGestao_receber['REPRESENTANTE'] == 'MG REPRESENTAÇOES')  ]
group_status_empresa_pago_terceiro =  frame_receber_pago_terceiro.groupby(['EMPRESA'])['VALOR'].sum()

# A RECEBER POR EMPRESA - TERCEIRO
frame_receber_previsto_terceiro = pGestao_receber[(pGestao_receber['STATUS'] == 'PREVISTO') & (pGestao_receber['REPRESENTANTE'] == 'LUPUS') | (pGestao_receber['REPRESENTANTE'] == 'MG REPRESENTAÇOES') ]
group_status_empresa_previsto_terceiro =  frame_receber_previsto_terceiro.groupby(['EMPRESA'])['VALOR'].sum()

# ATRASADO POR EMPRESA - TERCEIRO
frame_receber_atrasado_terceiro = pGestao_receber[(pGestao_receber['STATUS'] == 'ATRASADO') &  (pGestao_receber['REPRESENTANTE'] == 'LUPUS') | (pGestao_receber['REPRESENTANTE'] == 'MG REPRESENTAÇOES') ]
group_status_empresa_atrasado_terceiro =  frame_receber_atrasado_terceiro.groupby(['EMPRESA'])['VALOR'].sum()


# pGestao_datasets.info()
# print(pGestao_datasets['ANO MONTANTE'].unique().tolist())