
# entre com um número
# verifique se o número é positivo, negativo ou nulo

import streamlit as st

numero = st.number_input("Digite um número para verificar: ", step=1)

if numero >= 0:
    st.write(f"Número {numero} é positivo")
elif numero == 0:
    st.write(f"Número {numero} é nulo")
else:
    st.write(f"Número {numero} é negativo")