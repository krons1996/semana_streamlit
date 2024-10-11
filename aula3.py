import streamlit as st
import random

# crie um algoritimo que descubra um número secreto

# criar o número secreto
num_secreto = random.randint(1, 10)
# Título na aplicação
st.title("Jogo do Número Secreto")
# Dar uma mensagem de boas vindas
st.write("Boas-Vindas")
# receber o chute do usuário
chute = st.number_input("Digite um número de 1 à 10", min_value=1,max_value=10,step=1)
# verificar o chute com o número secreto
if st.button('Verificar'):
    if chute == num_secreto:       
# mostrar a mensagem personalizada
        st.balloons()
        st.success("Acertou! Descobriu o número secreto!")
    else:
        st.error("Errou!")