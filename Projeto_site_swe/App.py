import streamlit as st

st.set_page_config(page_icon="🍔", page_title="Lanchonete")

st.title("Minha Lanchonete")
st.write("Bem-vindo à nossa lanchonete!")

cardapio = {
    "Coxinha": 6,
    "Risole": 7,
    "Coca lata 350 ml": 3.5
}

# Criar carrinho
if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = []

# Escolher produto
st.subheader("Cardápio")

produto = st.selectbox("Escolha seu produto", cardapio.keys())

st.image(f"imagens/{produto}.jpg", width=250)

st.write("Preço: R$", cardapio[produto])

# Quantidade
quantidade = st.number_input("Quantidade", min_value=1, value=1)

# Adicionar produto
if st.button("Adicionar ao carrinho"):
    for i in range(quantidade):
        st.session_state["carrinho"].append(produto)

    st.success("Produto adicionado!")

# Mostrar carrinho
st.subheader("Meu carrinho")

if len(st.session_state["carrinho"]) > 0:

    total = 0

    for produto in cardapio:
        quantidade_produto = st.session_state["carrinho"].count(produto)

        if quantidade_produto > 0:
            preco = cardapio[produto] * quantidade_produto
            total = total + preco

            st.write(produto)
            st.write("Quantidade:", quantidade_produto)
            st.write("Preço: R$", preco)

    st.write("Total da compra: R$", total)

    # Forma de pagamento
    pagamento = st.selectbox(
        "Forma de pagamento",
        ["Pix", "Dinheiro", "Cartão de crédito", "Cartão de débito"]
    )

    # Finalizar pedido
    if st.button("Finalizar pedido"):
        st.success("Pedido realizado com sucesso!")
        st.write("Pagamento:", pagamento)
        st.write("Total: R$", total)

    # Limpar carrinho
    if st.button("Limpar carrinho"):
        st.session_state["carrinho"] = []
        st.rerun()

else:
    st.write("Seu carrinho está vazio.")