# Import required libraries
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

# Initialize global variables
indices_dict = {}
bitcoin = ['BTC-USD']
indices = ['S&P 500', 'Dow Jones', 'NASDAQ', 'NYSE']
indices_name = {'S&P 500': '^GSPC', 'Dow Jones': '^DJI', 'NASDAQ': '^IXIC', 'NYSE': '^NYA'}

# Function to download bitcoin data
def download_bitcoin_data():
    global bitcoin
    for index in bitcoin:
        try:
            indices_dict[f'{index}'] = yf.download(bitcoin, period='5y')
        except Exception as e:
            print(f'error while downloading the data for {index}')

# Function to download indices data
# param indices:
def download_data(indices):
    global indices_dict
    global indices_name
    for index in indices:
        index = indices_name[f'{index}']
        try:
            indices_dict[f'{index}'] = yf.download(index, period='5y')
        except Exception as e:
            print(f'error while downloading the data for {index}')

# Download data for bitcoin and indices
download_data(indices)
download_bitcoin_data()

# Function to create a comparison chart between bitcoin and indices
# param bitcoin:
# param indexs:
def create_chart(bitcoin, indexs):
    global indices_dict
    fig = go.Figure()

    # Add bitcoin trace
    for b in bitcoin:
        data = indices_dict[f'{b}']
        fig.add_trace(go.Scatter(x=data.index, y=data['Adj Close'].div((data['Adj Close'].iloc[0])).mul(100), name='bitcoin'))

    # Add indices traces
    for index in indexs:
        if index != 'BTC-USD':
            index_symb = indices_name[f'{index}']
        data = indices_dict[f'{index_symb}']
        fig.add_trace(go.Scatter(x=data.index, y=data['Adj Close'].div((data['Adj Close'].iloc[0])).mul(100), name=index))

    # Configure chart title, axis labels, and legend design
    fig.update_layout(title=f'Comparision charts',yaxis_title='Price (USD)',xaxis_title = 'Time',
                      legend=dict(
                      font=dict(
                          family="Courier",
                          size=12,
                          color="White"),
                      bgcolor="LightSteelBlue",
                      bordercolor="Black",
                      borderwidth=2,
                      title=dict(
                          text='Indices compare with Bitcoin',
                          font=dict(
                              family="Times New Roman",
                              size=14,
                              color="White"
                          )
                      )
                  ))
    return fig

# Main function to create a Streamlit app
# param sidebar_multiselect_placeholder: For creating multiselect sidebar
def main(sidebar_multiselect_placeholder):
    global bitcoin
    global indices
    global indices_dict
    global indices_name

    st.empty()

    with st.sidebar:
        sidebar_multiselect_placeholder.header('Lets Compare US\'s indices with bitcoin performance')
        indexs = sidebar_multiselect_placeholder.multiselect('Which index do you want to compare with Bitcoin?', indices)

    # Create and display the chart
    chart = create_chart(bitcoin=bitcoin, indexs=indexs)
    st.plotly_chart(chart, use_container_width=True)