import streamlit as st
import time

if "name" not in st.session_state:
    st.session_state.name = "User"
if "email" not in st.session_state:
    st.session_state.email = "Not provided"

st.image("userprof.png", width=150)

col1, col2 = st.columns([3, 1])

with col1:
    st.title("Account Information")
st.subheader(f"Name: {st.session_state.name}", divider="orange")
st.subheader(f"Email: {st.session_state.email}", divider="orange")

with col2:
    with st.popover("Edit Account Info"):
        st.subheader("Edit Account Information")
        name = st.text_input("Name", value=st.session_state.name, placeholder="Enter your name")
        email = st.text_input("Email", value=st.session_state.email, placeholder="johndoe@example.com")
        conButton = st.button("Save Changes", type="primary", width="stretch")

        if conButton:
            if not name or not email:
                st.error("Please fill in all fields.")
            elif "@" not in email or "." not in email:
                st.error("Please enter a valid email address.")
            else:
                st.success("Account information updated successfully!")
                st.session_state.name = name
                st.session_state.email = email
                with st.status("Updating profile..."):
                    st.write("Updating profile...")
                    time.sleep(2)
                st.rerun() 