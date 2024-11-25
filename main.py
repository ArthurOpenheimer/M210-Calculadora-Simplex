import streamlit as st
from programacao_linear import pLinear

st.title("Calculadora Simplex")
st.sidebar.title("Entrada de Dados")

#Arredondamento de valores decimais
def validate_decimal(value, key):
    if value is not None:
        rounded_value = round(value, 4)
        return rounded_value
    return value

#Entrada de Dados
num_variaveis = st.sidebar.number_input("Número de variáveis", min_value=1, step=1, key="num_variaveis")
num_restricoes = st.sidebar.number_input("Número de restrições", min_value=1, step=1, key="num_restricoes")

st.sidebar.subheader("Coeficientes da F.O.")
coeficientes_fo = []
for i in range(int(num_variaveis)):
    coef = validate_decimal(
        st.sidebar.number_input(f"Coeficiente de X{i+1}", key=f"coef_fo_{i}"),
        key=f"coef_fo_{i}",
    )
    coeficientes_fo.append(coef)

st.sidebar.subheader("Coeficientes das Restrições")
restricoes = []
for i in range(int(num_restricoes)):
    st.sidebar.write(f"Restrição {i+1}")
    restricao = []
    for j in range(int(num_variaveis)):
        coef = validate_decimal(
            st.sidebar.number_input(f"Coeficiente de X{j+1} (Restrição {i+1})", key=f"coef_{i}_{j}"),
            key=f"coef_{i}_{j}",
        )
        restricao.append(coef)
    limite = validate_decimal(
        st.sidebar.number_input(f"Limite (Restrição {i+1})", key=f"limite_{i}"),
        key=f"limite_{i}",
    )
    sinal = st.sidebar.selectbox(f"Sinal (Restrição {i+1})", ("<=",">="), key=f"sinal_{i}")
    restricao.append(sinal) #Adiciona o sinal da restrição
    restricao.append(limite)  #Adiciona o limite como última coluna
    restricoes.append(restricao)

#Exibição de Dados
st.header("Função Objetivo")
fo = " + ".join([f"{coeficientes_fo[i]} X{i+1}" for i in range(len(coeficientes_fo))])
st.write(f"Max Z = {fo}")

st.header("Restrições")

with st.expander("Propor Alterações", expanded=False):
    st.write("Propor alterações nas restrições")
    for i, restricao in enumerate(restricoes):
        st.write(f"Restrição {i+1}")
        alteracao = validate_decimal(
            st.number_input(f"Alteração no limite", key=f"alt_{i}"),
            key=f"alt_{i}",
        )
        restricoes[i][-1] += alteracao  #Aplica a alteração ao limite
    if st.button("Verificar Viabilidade"):
        from programacao_linear import verify_viability, pLinear
        viavel, restricoes_inviaveis = verify_viability(restricoes)
        if viavel:
            try:
                result = pLinear(int(num_variaveis), coeficientes_fo, restricoes)
                st.success("As alterações propostas são viáveis")
                st.write(f"Novo Lucro Ótimo (Z) = {result[1]} reais")
            except Exception as e:
                st.error(f"Erro ao calcular o novo lucro: {e}")
        else:
            for restricao_inviavel in restricoes_inviaveis:
                st.error(f"Não é viável devido à alteração na restrição X{restricao_inviavel}")

for i, restricao in enumerate(restricoes):
    coef = restricao[:-2]  #Exclui o limite e o sinal para montar a inequação
    limite = restricao[-1]
    sinal = restricao[-2]
    if all([c == 0 for c in coef]):
        continue
    restricao_str = " + ".join([f"{coef[j]} X{j+1}" for j in range(len(coef)) if coef[j] != 0])
    st.write(f"{restricao_str} {sinal} {limite}")

string = ""
for j in range(len(coeficientes_fo)):
    string += f"X{j+1}, "
string = string[:-2]
string += " >=0"
st.write(string)

#Botão para calcular a solução
if st.button("Calcular Solução"):
    nvar = int(num_variaveis)
    f_obj = coeficientes_fo
    rest = restricoes
    try:
        #Chamada da função pLinear
        result = pLinear(nvar, f_obj, rest)

        #Exibe os resultados
        st.subheader("Solução Ótima")
        for i, valor in enumerate(result[0]):
            st.write(f"X{i+1} = {valor}")
        st.write(f"Lucro Ótimo (Z) = {result[1]}")

        #Exibe os preços sombra
        st.subheader("Preços Sombra")
        for i, preco in enumerate(result[2]):
            st.write(f"Restrição {i+1}: {preco} reais")
    except Exception as e:
        st.error(f"Ocorreu um erro ao calcular a solução: {e}")
