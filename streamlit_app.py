import streamlit as st
import pandas as pd
import datetime

securities_data = pd.read_csv('securitiesData.csv')

portfolio_data = []

st.title("Portfolio Tracker")

st.header("Add Security")
with st.form("add_security"):
    security = st.selectbox("Security", securities_data['Security'])
    entry_price = st.number_input("Entry Price")
    quantity = st.number_input("Quantity")
    target_price = st.number_input("Target Price")
    notes = st.text_area("Notes")
    expected_holding_period = st.text_input("Expected Holding Period")
    submitted = st.form_submit_button("Add to Portfolio")

if submitted:
    date_added = datetime.date.today()
    target_returns = (target_price - entry_price) / entry_price * 100
    trading_days_elapsed = 0
    portfolio_data.append({
        'Security': security,
        'Entry Price': entry_price,
        'Quantity': quantity,
        'Date Added': date_added,
        'Target Price': target_price,
        'Target Returns': target_returns,
        'Trading Days Elapsed': trading_days_elapsed,
        'Notes': notes,
        'Expected Holding Period': expected_holding_period
    })

st.header("Portfolio")
if portfolio_data:
    df = pd.DataFrame(portfolio_data)
    st.write(df)
else:
    st.write("No securities added to portfolio.")

st.header("Delete Security")
with st.form("delete_security"):
    index = st.selectbox("Select security to delete", range(len(portfolio_data)))
    submitted = st.form_submit_button("Delete")

if submitted:
    del portfolio_data[index]

if __name__ == "__main__":
    st.run()
