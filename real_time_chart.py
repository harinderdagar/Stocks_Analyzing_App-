# Import required libraries and modules
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st
import time
import threading

_running = threading.Event()

# Function to fetch data for the specified ticker, interval, and period
# param ticker: Stocks' Ticker
# param interval: Time granulity for which data is requried
# param period: No of days or months or years
def fetch_data(ticker, interval='1m', period='1d'):
    try:
        data = yf.download(ticker, interval=interval, period=period)
    except Exception as e:
        print(f'error while downloading the data for {ticker}') 
    return data

# Function to create a line chart for the provided data and ticker
# param data: data of the stocks
# param ticker: Stocks' Ticker
def create_chart(data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Close', line=dict(color='royalblue', width=1)))
    fig.update_layout(title=f'{ticker} Real-Time Line Chart', yaxis_title='Price', xaxis_title='Time')
    return fig

# Function to check if the chart update loop is running
def is_running():
    return _running.is_set()

# Main function that runs real time chart page
# param sidebar_select_placeholder: Create the sidebar
def main(sidebar_select_placeholder):
    # In the main function setting the "_running" flag  which control the while loop
    _running.set()
    st.empty()
    st.write("This chart updates every minute with the latest data from Yahoo Finance.")

    #tickers = ['^NZ50', '^AXJO']
    tickers = ['^NZ50']
    update_interval = 60  # Update every minute
    with st.sidebar:
        ticker = sidebar_select_placeholder.selectbox('Select the stocks you want to display.', tuple(tickers))

    if ticker:
        data = fetch_data(ticker)
        chart = create_chart(data, ticker)
        chart_placeholder = st.plotly_chart(chart, use_container_width=True)

        # Update the chart every minute with the latest data
        while is_running():
            time.sleep(update_interval)
            data = fetch_data(ticker)
            chart = create_chart(data, ticker)
            chart_placeholder.plotly_chart(chart, use_container_width=True)

# Exiting the main function unsetting the "_running" flag which in turn stop the while loop
    _running.clear()
