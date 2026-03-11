import streamlit as st

st.title("About This App")
st.subheader("What is PeraLista?", text_alignment="left", divider="orange",  width="content")
st.markdown('''PeraLista is a personal financial management app made to help you track your :blue-background[income and expenses, record transactions, see insights, and manage account information]. It is tailored to be simple, user-friendly, and easy to navigate.''', text_alignment="justify")

st.subheader("Our Target Users", divider="orange", text_alignment="left", width="content")
st.markdown ('''PeraLista is specifically designed for :blue-background[individuals who want to start managing their finances]. This application is ideal for individuals who are looking for a simple and clean financial tracker UI. ''', text_alignment="justify")

st.subheader("Key Features", divider="orange", text_alignment="left", width="content")
st.markdown('''PeraLista takes :blue-background[username, email, income, and expenses as input and displays it through graphs and structured text formats such as total income, total expenses, current balance, and transacti on history.] ''', text_alignment="justify")
st.subheader("UI components used", divider="orange", text_alignment="left", width="content")

col1, col2 = st.columns(2)

with col1:
    st.markdown(""" 
- `st.sidebar.image`  
- `st.sidebar.title`  
- `st.Page`  
- `st.navigation`  
- `pg.run`  
- `st.container`  
- `st.title`  
- `st.header`  
- `st.subheader`  
- `st.columns`  
- `st.tabs`  
- `st.popover`
    """)

with col2:
    st.markdown("""
- `st.bar_chart`  
- `st.number_input`  
- `st.date_input`  
- `st.selectbox`  
- `st.text_input`  
- `st.button`  
- `st.status`  
- `st.success`  
- `st.error`  
- `st.image`  
- `st.markdown`  
- `st.write`
    """)


