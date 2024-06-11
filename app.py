import pandas as pd
import streamlit as st

st.title('DEMO')

tickers = ['AAPL', 'DIS', 'NKE', 'NFLX']
pick = st.sidebar.selectbox("Pick ticker", tickers)
st.write("You picked " + pick)

startDate = st.date_input("Pick a start date")
