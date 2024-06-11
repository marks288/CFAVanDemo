import pandas as pd
import streamlit as st
import plotly.express as px

st.title('DEMO')

tickers = ['AAPL', 'DIS', 'NKE']
pick = st.sidebar.selectbox("Pick ticker", tickers)
st.write("You picked " + pick)

startDate = st.sidebar.date_input("Pick a start date")
endDate = st.sidebar.date_input("Pick an end date")

df = pd.read_csv(pick + ".csv", parse_dates=['Date'])
st.write(df)

dayStart = '{:%Y-%m-%d}'.format(startDate)
dayEnd = '{:%Y-%m-%d}'.format(endDate)
filterDF = df[df['Date'].between(dayStart, dayEnd)]

fig = px.line(filterDF, x='Date', y='Close')
st.plotly_chart(fig)
