import pandas as pd
import streamlit as st

st.title('DEMO')

tickers = ['AAPL', 'DIS', 'NKE']
pick = st.sidebar.selectbox("Pick ticker", tickers)
st.write("You picked " + pick)

startDate = st.sidebar.date_input("Pick a start date")
endDate = st.sidebar.date_input("Pick an end date")

df = pd.read_csv(+ pick + ".csv")
st.write(df)
