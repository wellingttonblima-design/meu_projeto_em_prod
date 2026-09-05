import streamlit as st
import pandas as pd

#procoding = não usar ia generativa para construir códigos

df_vendas = pd.read_csv('vendas.csv')

st.header("Calculadora streamlit")
st.write("ADICIONE OS NÚMEROS INTEIROS PARA CALCULAR: ")

n1 = int(st.number_input('Digite o primeiro número: ', value = 0, label_visibility = 'hidden')) #'label_visibility' serve não mostrar o testo no site.
n2 = int(st.number_input('Digite o segundo número: ', value = 0, label_visibility = 'hidden'))



soma_, sub_, mult_, div_, = st.columns(4) #Para alinhar cada botão


if soma_.button('+'):
    soma = n1 + n2
    st.info(f'Resultado: {soma}')
elif sub_.button('-'):
    sub = n1 - n2
    st.info(f'Resultado: {sub}')
if mult_.button('X'):
    mult = n1 * n2
    st.info(f'Resultado: {mult}')
elif div_.button(':'):
    if n1 == 0 or n2 == 0:
        st.info('Impossível dividir por zero! Digite outro número')
    else:
        div = n1 / n2
        st.info(f'Resultado: {div}')

if st.button('Abrir Mapa'):
    map = st.map()
    if st.button('Fechar Mapa'):
        map = st.empty()


st. header('Analise de Dados')
if st.button('Abrir Analise de Dados'):
    dados = [
    {st.table(df_vendas)},
    {st.bar_chart(df_vendas, x = 'ano', y = 'lucro')},
    {st.scatter_chart(df_vendas, x = 'venda', y = 'lucro')},
    {st.line_chart(df_vendas, x = 'ano', y = 'lucro')}
    ]
    if st.button('Fechar Analise de Dados'):
        st.empty()
