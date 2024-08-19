import pandas as pd 

# TABELA DE DEXTRATO DE CREDITO PLANILHA DE GESTAO ----------------------------------------------------
tabela_extratolupus = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSd_0XR8nI68FKDUWTQDnUhs8cLxfhFsvQY-wS4u0DyReTvUjgZ95aWKEPzaJ8wvnNcQZgEs4UDJgiw/pub?gid=995652507&single=true&output=csv')
tabela_extratolupus = tabela_extratolupus.drop(columns=['Unnamed: 8',' VALOR TOTAL '])
tabela_extratolupus = tabela_extratolupus.rename(columns={'Unnamed: 7' : 'VALOR'})
tabela_extratolupus.columns = tabela_extratolupus.columns.str.strip()
transform_columns_tb_extratolupus = ['VALOR']
tabela_extratolupus[transform_columns_tb_extratolupus] = tabela_extratolupus[transform_columns_tb_extratolupus].apply(
    lambda col: col.str.replace('.','').str.replace(',','.').astype(float)
)
tabela_extratolupus = tabela_extratolupus.drop(index=0)
tabela_extratolupus['DATA'] = pd.to_datetime(tabela_extratolupus['DATA'], format='%d/%m/%Y').dt.date

# ----------------------------------------------------------------------------------------------
