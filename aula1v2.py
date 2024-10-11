import streamlit as st
import requests
import pandas as pd
import plotly.express as px


st.title("DASHBOARD DE VENDAS :shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())
receita = df['Preço'].sum()
venda = df.shape[0]
coluna = df.shape[1]

def simplifica_num(num):
    if num >= 1000000000:
        num = float(round(num/ 1000000000, 2))    
        return f"{num} bilhões"
    elif num >= 1000000:
        num = float(round(num/ 1000000, 2))    
        return f"{num} milhões"
    elif num >= 1000:
        num = float(round(num/ 1000, 2))    
        return f"{num} mil"
    else:
        return f"{num}"



if st.button("todos"):
    st.balloons()    
    st.metric('Receita R$', simplifica_num(receita))
    st.metric('Quantidade de vendas (linhas)',simplifica_num(venda))
    st.metric('Quantidade de vendas (colunas)',simplifica_num(coluna))
    st.dataframe(df)
else:
    st.write("clique no botão todos")
