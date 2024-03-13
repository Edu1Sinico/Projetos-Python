import pandas as pd

igm_df = pd.read_csv("Biblioteca-Panda-7/dados/igm_modificado.csv")
ind_des = igm_df['indice_governanca']

















print("Exibe toda a tabela:\n",igm_df,"\n")
print("Conta quantas linhas e colunas ela possuí:\n",igm_df.shape,"\n")
print("Verifica os tipos das colunas:\n",igm_df.info(),"\n")
print("",igm_df.head(),"\n")
print("",igm_df.tail(),"\n")
print("",igm_df.sample(5),"\n")
print("",igm_df.sample(5).T,"\n")
print("",igm_df[0:5].T,"\n")
print("",igm_df[-5:].T,"\n")
print("",igm_df[20:30].T,"\n")
print("",igm_df['porte'],"\n")
print("",igm_df[['municipio','indice_governanca']],"\n")
print("",type(igm_df['porte']),"\n")
print("",ind_des.count(),"\n")
print("",ind_des.size,"\n")
print("",ind_des.isnull(),"\n")
print("",ind_des.isnull().sum(),"\n")
print("",ind_des.dropna(),"\n")
print("",ind_des.isnull().sum(),"\n")
print("",ind_des.dropna(inplace=True),"\n")
print("",ind_des.isnull().sum(),"\n")
print("",ind_des.min(),"\n")
print("",ind_des.max(),"\n")
print("",ind_des.mean(),"\n")
print("",ind_des.std(),"\n")
print("",ind_des.describe(),"\n")
print("",igm_df.describe(),"\n")
print("",igm_df[igm_df['regiao'] == 'SUL'],"\n")
