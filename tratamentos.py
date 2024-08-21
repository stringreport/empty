import pandas as pd 

# TABELA DE DEXTRATO DE CREDITO PLANILHA DE GESTAO ----------------------------------------------------
tabela_extratolupus = pd.read_csv('https://docs.google.com/spreadsheets/d/1jmJuCg80ccjQVnziWGK7V1r4Tyernxp7kXZkcBXz-qg/pub?gid=995652507&single=true&output=csv')
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
