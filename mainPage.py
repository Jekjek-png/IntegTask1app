import streamlit as st

if "name" not in st.session_state:
    st.session_state.name = "User"
if "email" not in st.session_state:
    st.session_state.email = ""
if "balance" not in st.session_state:
    st.session_state.balance = 0.0
if "transactions" not in st.session_state:
    st.session_state.transactions = []

st.sidebar.image("logo.png", width=200)
st.sidebar.title("PeraLista", text_alignment="center")


pages = {
    "Menu": [
        st.Page("dashBoard.py", title="Dashboard"),
        st.Page("accountPage.py", title="Account"),
        st.Page("about.py", title="About"),
    ]
}

pg = st.navigation(pages)

pg.run()