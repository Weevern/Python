import yfinance as yf
import streamlit as st

st.write("""
# App that shows stock price
Shown are the stock closing price and volume of Google
""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-10-15')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# Command line -> streamlit run app.py
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
