import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from millify import millify


st.title("DASHBOARD DE VENDAS :shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())
receita = df['Preço'].sum()
vendas = df.shape[0]

if st.button("todos"):
    st.balloons()    
    st.metric('Receita R$', millify(receita, precision=2))
    st.metric('Quantidade de vendas (linhas)',millify(vendas, precision=2))
    st.metric('Quantidade de vendas (colunas)',df.shape[1])
    st.dataframe(df)
else:
    st.write("clique no botão todos")
