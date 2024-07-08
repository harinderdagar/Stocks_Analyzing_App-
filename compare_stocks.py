# Import required libraries
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import pandas_ta as ta
import streamlit as st

# Initialize the stocks dictionary
stocks_dict = {}

# List of stock tickers to be used
tickers = ['AAPL', 'MSFT', 'IBM', 'AMZN', 'META']

# Function to download stock data for given tickers
# param tickers: Stocks' Tickers
def download_data(tickers):
    global stocks_dict
    for ticker in tickers:
        try:
            # Download stock data for the past 5 years and store it in the stocks_dict
            stocks_dict[f'{ticker}'] = yf.download(ticker, period='5y')
        except Exception as e:
            print(f'error while downloading the data for {ticker}')

# Call the download_data function with the tickers list
download_data(tickers)

# Function to generate a line chart for the selected stocks
# param stocks:
def print_line_chart(stocks):
    global stocks_dict
    fig = go.Figure()

    # Add a trace for each stock to the line chart
    for stock in stocks:
        df = stocks_dict[f'{stock}']
        fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'].div((df['Adj Close'].iloc[0])).mul(100), name=stock))

    # Update layout for the line chart
    fig.update_layout(title=f'Comparision charts', yaxis_title='Price (USD)', xaxis_title='Time',
                      legend=dict(
                          font=dict(
                              family="Courier",
                              size=12,
                              color="White"),
                          bgcolor="LightSteelBlue",
                          bordercolor="Black",
                          borderwidth=2,
                          title=dict(
                              text='Stock Compare',
                              font=dict(
                                  family="Times New Roman",
                                  size=14,
                                  color="White"
                              )
                          )
                      ))
    return fig

# Main function to display the line chart on the Streamlit app
# param sidebar_multiselect_placeholder: For creating multiselect sidebar
def main(sidebar_multiselect_placeholder):
    global tickers
    # Create a sidebar section for selecting stocks to compare
    with st.sidebar:
        sidebar_multiselect_placeholder.header('Lets Compare stocks charts')
        stocks = sidebar_multiselect_placeholder.multiselect('Which company stocks Do you want to compare?', tickers)
    # Display the line chart for the selected stocks
    if stocks:
        st.plotly_chart(print_line_chart(stocks), use_container_width=True)