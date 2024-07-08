# Import required libraries
import pandas as pd
import yfinance as yf
import plotly.subplots as ms
import plotly.graph_objects as go
import pandas_ta as ta
import streamlit as st

# Initialize the stocks dictionary
stocks_dict = {}
# List of stock tickers to be used
tickers = ['AAPL', 'MSFT', 'IBM', 'AMZN', 'META']

# Function to download stock data for given tickers and store in stocks_dict
# param tickers: List of stocks' ticker
def init_stocks_data(tickers):
    global stocks_dict
    for ticker in tickers:
        try:
            stocks_dict[f'{ticker}'] = yf.download(ticker, period='2y')
        except Exception as e:
            print(f'error while downloading the data for {ticker}')

# Call the init_stocks_data function with the tickers list
init_stocks_data(tickers)

# Main function to display the charts on the Streamlit app
# param sidebar_select_placeholder: Create a new sidebar
def main(sidebar_select_placeholder):
    # Function to determine volume bar colors based on price change
    def volume_colors(df):
        colors = []
        for i in range(len(df['Adj Close'])):
            if i != 0:
                if df['Adj Close'][i] > df['Open'][i]:
                    colors.append('Green')
                else:
                    colors.append('Red')
            else:
                colors.append('Red')
        return colors

    # Function to generate a line chart for a single stock
    # param stock: 
    def print_line_chart(stock):
        df = stocks_dict[f'{stock}']
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'], name='Price', line=dict(color='royalblue', width=1)))
		#Update the title and axis labels
        fig.update_layout(title=f'{stock} Stock line chart', yaxis_title='Price (USD)', xaxis_title='Time')

        return fig

    # Function to generate a candlestick and volume chart for a single stock
    # param stock: 
    def print_Candlestick_chart(stock):
        df = stocks_dict[f'{stock}']
		# Create two sublplots
        fig = ms.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
		# Add Bar chart on the first subplot
        fig.add_trace(go.Bar(x=df.index, y=df['Volume'], marker_color=volume_colors(df), name='Bar'), row=2, col=1)
		# Add CandleStick chart on the first subplot
        fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Adj Close'], name='Candlestick'), row=1, col=1)
		#Configure chart title, axis labels, and legend design
        fig.update_layout(title=f'{stock} Stock Candlestick and Volume chart', yaxis1_title='Price (USD)',
                          yaxis2_title='Volume(Millions)', xaxis2_title='Time',
                          xaxis1_rangeslider_visible=False, xaxis2_rangeslider_visible=False,
                          legend=dict(
                              font=dict(
                                  family="Courier",
                                  size=12,
                                  color="White"),
                              bgcolor="LightSteelBlue",
                              bordercolor="Black",
                              borderwidth=2,
                              title=dict(
                                  text='Charts',
                                  font=dict(
                                      family="Times New Roman",
                                      size=14,
                                      color="White"
                                  )
                              )
                          ))
        return fig

    # Function to generate a simple moving average (SMA) chart for a single stock
    # param stock: 
    def print_ema_sma_chart(stock):
        df = stocks_dict[f'{stock}']
        fig = go.Figure()
		#Add Line chart
        fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'], name='Adj Close Price', line=dict(color='#008080', width=2)))
		#Add SMA50 chart
        fig.add_trace(go.Scatter(x=df.index, y=ta.sma(df['Adj Close'], length=50), name='SMA50', line=dict(color='#b74160', width=2)))
		#Add SMA100 chart
        fig.add_trace(go.Scatter(x=df.index, y=ta.sma(df['Adj Close'], length=100), name='SMA100', line=dict(color='#7c501a', width=2)))
		#Configure chart title, axis labels, and legend design
        fig.update_layout(title=f'{stock} Stock SMA charts',
                          legend=dict(
                              font=dict(
                                  family="Courier",
                                  size=12,
                                  color="White"),
                              bgcolor="LightSteelBlue",
                              bordercolor="Black",
                              borderwidth=2,
                              title=dict(
                                  text='SMA',
                                  font=dict(
                                      family="Times New Roman",
                                      size=14,
                                      color="White"
                                  )
                              )
                          ))
        return fig

    # Function to generate a Relative Strength Index (RSI) chart for a single stock
    # param stock: 
    def print_rsi_chart(stock):
        df = stocks_dict[f'{stock}']

		# Create two sublplots
        fig = ms.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.09)
		# Add line chart on the first subplot
        fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], name="Adj Close"), row=1, col=1)
        # Add RSI chart on the 2nd subplot
        fig.add_trace(go.Scatter(x=df.index, y=ta.rsi(df['Adj Close']), name="RSI_14", line=dict(color='purple')), row=2, col=1)
		
		#Update the title and design, and add horizontal lines at 30% and 70% in the second subplot. Additionally, customize the legend and incorporate it into the second subplot.
        fig.update_layout(title=f'Adj Close Price and RSI for {stock}', yaxis1_title='Price (USD)',
                          yaxis2_title='Percentage(%)', xaxis2_title='Time',
                          xaxis1_rangeslider_visible=False, xaxis2_rangeslider_visible=False,
                          shapes=[dict(
                              type="line", xref="paper", yref="y2", x0=0, y0=70, x1=1, y1=70, line=dict(color="red", width=2, dash="dash")),
                              dict(type="line", xref="paper", yref="y2", x0=0, y0=30, x1=1, y1=30, line=dict(color="green", width=2, dash="dash"))
                          ],
                          annotations=[dict(
                              xref="paper", yref="y2", x=0.005, y=74, text="Overbought > 70%", showarrow=False, font=dict(family="Arial", size=14, color="red")),
                              dict(
                                  xref="paper", yref="y2", x=0.01, y=34, text="Oversold < 30%", showarrow=False, font=dict(family="Arial", size=14, color="green"))
                          ],
                          legend=dict(
                              font=dict(
                                  family="Courier",
                                  size=12,
                                  color="White"),
                              bgcolor="LightSteelBlue",
                              bordercolor="Black",
                              borderwidth=2,
                              title=dict(
                                  text='RSI',
                                  font=dict(
                                      family="Times New Roman",
                                      size=14,
                                      color="White")
                              ))
                          )
        return fig

    # Create a sidebar section for selecting a stock
    with st.sidebar:
        select_column = sidebar_select_placeholder.selectbox('Select the stocks you want to display.', tuple(tickers))
    # Display the charts for the selected stock
    if select_column:
        st.plotly_chart(print_line_chart(select_column), use_container_width=True)
        st.plotly_chart(print_Candlestick_chart(select_column),use_container_width=True)
        st.plotly_chart(print_ema_sma_chart(select_column), use_container_width=True)
        st.plotly_chart(print_rsi_chart(select_column), use_container_width=True)