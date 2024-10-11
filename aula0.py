import streamlit as st



idade = st.number_input("Digite sua idade:", min_value=14, max_value=120)

if idade >= 18:
    st.write(f"Alô Mundo - você é maior de idade: {idade} anos")
else:
    st.write(f"Alô Mundo - você é menor de idade: {idade} anos")
