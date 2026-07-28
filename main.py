import pandas  as pd
import streamlit as st

dados = pd.read_cvs('dados.cvs')

print(dados)

st.header('Analise de vendas')

df= pd.DataFrame(dados)

st.bar_chart(df, x = 'vendedor', y = 'vendas' )

x = np.array([ 
  
  [1,5],
  [1,3],
  [2,5]])

# import pandas as pd 
# import streamlit as st
from sklearn.tree import DecisionTreeClassifier
# import numpy as np


# dados =  pd.read_csv('dados.csv')
# print(dados)
# st.header('Analise de Vendas')
# df = pd.DataFrame(dados)
# # st.bar_chart(df, x = 'vendedor', y = 'vendas' )


# X = np.array([df['vendas'], df['ano']])
# y = np.array([df['vendas']])


# model= DecisionTreeClassifier()
# m = model.fit(X,y)


# print(m.predict([[10000, 2027]]))



# NOTAS DE dados 


import streamlit as st
import pandas as pd
# from sklearn.linear_model import LinearRegression



dados_ = pd.read_csv('dados.csv')
print(dados_)


# st.header('ANALISE DE NOTAS - PREVENDO')



x  =  list(dados_['horas_nas_redes'])
print(x)
y  = list(dados_['aprovados_curso'])
print(y)


dados = pd.DataFrame({
'horas_nas_redes':x,
'aprovados':y
})


print(dados)


# st.scatter_chart(dados, x = 'ano', y= 'vendas')
modelo_escola = DecisionTreeClassifier() 
modelo_escola.fit(dados[['horas_nas_redes']], dados['aprovados'])


h_estudo = st.number_input('Digite a quantidade de horas nas redes sociais ')
nota_final = modelo_escola.predict([[h_estudo]])
print(nota_final)


st.metric(f'Resultado ' ,f'{min(nota_final[0],1):.1f}')