import streamlit as st
import pandas as pd
import time
from numpy.random import default_rng as rng

if "transactions" not in st.session_state:
    st.session_state.transactions = []
if "balance" not in st.session_state:
    st.session_state.balance = 0.0
if "name" not in st.session_state:
    st.session_state.name = ""


with st.container(border=True):
    st.title("Dashboard")
    col1, col2 = st.columns([3, 3])

    with col1:
        with st.container(border=True, height=385):
            gcol1, gcol2, gcol3 = st.columns([1, 2, 1])
        with gcol2:
            st.title(f"Hello! {st.session_state.name}")
            st.subheader(f"Your balance is: ₱{st.session_state.balance:.2f}",  divider="orange")

    with col2:
        with st.container(border=True, height=385):
            with st.container(border=True):
                st.header("Total Income")
                total_income = sum(t["Amount"] for t in st.session_state.transactions if t["Type"] == "Income")
                st.subheader(f"₱{total_income:.2f}",  divider="green")

            with st.container(border=True):    
                st.header("Total Expenses")
                total_expenses = sum(t["Amount"] for t in st.session_state.transactions if t["Type"] == "Expenses")
                st.subheader(f"₱{total_expenses:.2f}", divider="red")

with st.container(border=True):
    st.title("Quick Actions")
    tab1, tab2, tab3, tab4 = st.tabs(["Money in", "Money out", "Transactions", "Insights"])
 
    with tab1:
        with st.container(border=True, height=475):
            st.header("Money in")
            amount_in = st.number_input("Amount of money coming in:", value=0, key="money_in_input")
            date_in = st.date_input("Date of the transaction", key="date_in")
            cat_in = st.selectbox("Category", ("Allowance", "Salary", "Extra income"),
                                  index=None, placeholder="Select category...")
            note_in = st.text_input("Note for the transaction", key="note_in")

        if st.button("Money in", type="primary", use_container_width=True):
            if amount_in <= 0:
                st.error("Please enter a positive amount")
            else:
                st.session_state.balance += amount_in
                st.success(f"Added ₱{amount_in:.2f} on {date_in}. "
                           f"Your new balance is: ₱{st.session_state.balance:.2f}")
                st.session_state.transactions.append({
                    "Type": "Income",
                    "Amount": amount_in,
                    "Date": date_in,
                    "Category": cat_in,
                    "Note": note_in
                })

                with st.status("Updating dashboard..."):
                    st.write("Updating dashboard...")
                    time.sleep(1)

                st.rerun() 

    with tab2:
        with st.container(border=True, height=475):
            st.header("Money out")
            amount_out = st.number_input("Amount of money going out:", value=0, key="money_out_input")
            date_out = st.date_input("Date of the transaction", key="date_out")
            cat_out = st.selectbox("Category", ("Transportation", "Food", "Shopping"),
                                   index=None, placeholder="Select category...")
            note_out = st.text_input("Note for the transaction", key="note_out")

        if st.button("Money out", type="primary", use_container_width=True):
            if amount_out <= 0:
                st.error("Please enter a positive amount")
            elif amount_out > st.session_state.balance:
                st.error("Insufficient balance.")
            else:
                st.session_state.balance -= amount_out
                st.success(f"Deducted ₱{amount_out:.2f} on {date_out}. "
                           f"Your new balance is: ₱{st.session_state.balance:.2f}")
                st.session_state.transactions.append({
                    "Type": "Expenses",
                    "Amount": amount_out,
                    "Date": date_out,
                    "Category": cat_out,
                    "Note": note_out
                })
                with st.status("Updating dashboard..."):
                    st.write("Updating dashboard...")
                    time.sleep(1)
                st.rerun() 
                 

    with tab3:
        with st.container(border=True, height=475):
            st.header("Transactions")
            header_cols = st.columns(5)
            headers = ["Type", "Amount", "Date", "Category", "Note"]
            for col, header in zip(header_cols, headers):
                col.markdown(f"**{header}**")
            for transaction in st.session_state.transactions:
                row_cols = st.columns(5)
                row_cols[0].write(transaction["Type"])
                row_cols[1].write(f"₱{transaction['Amount']:.2f}")
                row_cols[2].write(transaction["Date"].strftime("%Y-%m-%d"))
                row_cols[3].write(transaction["Category"])
                row_cols[4].write(transaction["Note"])

    with tab4:
        with st.container(border=True, height=475):
             st.title("Income Vs Expenses")

             with st.container():
                 if st.session_state.transactions:
                    df = pd.DataFrame(st.session_state.transactions)
                 else:
                    df = pd.DataFrame({
                "Type": ["Expenses", "Income"],
                "Amount": [0, 0]
            })
                 st.bar_chart(df, x="Type", y="Amount", use_container_width=True)