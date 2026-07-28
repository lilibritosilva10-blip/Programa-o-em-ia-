
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título do Aplicativo
st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# Treinamento do Modelo de Regressão Linear
modelo_vendas = LinearRegression()
modelo_vendas.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

# Visualização dos dados passados (Gráfico de Dispersão / Linha)
st.subheader("Histórico de Investimento vs Faturamento")
st.line_chart(dados_vendas, x='investimento', y='faturamento')

# Interatividade com o Usuário (Controle Deslizante / Slider)
investimento_usuario = st.slider(
    'Selecione o valor do investimento em propaganda (R$):',
    min_value=0,
    max_value=1000,
    value=300,
    step=50
)

# Previsão
faturamento_previsto = modelo_vendas.predict([[investimento_usuario]])

# Exibição do Resultado
st.metric(
    label="Faturamento Estimado",
    value=f"R$ {faturamento_previsto[0]:,.2f}"
)



import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Previsão de Vendas")

# Base de dados historica
df = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# Separando x e y pro modelo
X = df[['investimento']]
y = df['faturamento']

# Treinando a regressao linear
modelo = LinearRegression()
modelo.fit(X, y)

# Interface
st.write("Digite o valor do investimento para prever o faturamento:")

valor_investido = st.number_input("Valor em Marketing (R$)", min_value=0.0, value=300.0)

if st.button("Prever"):
    previsao = modelo.predict([[valor_investido]])[0]
    st.success(f"Faturamento estimado: R$ {previsao:.2f}")

# Mostra a tabela e o grafico simples dos dados
st.subheader("Dados Históricos")
st.dataframe(df)
st.line_chart(df.set_index('investimento'))