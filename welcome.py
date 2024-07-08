import streamlit as st

#def home_page(container):
def welcome_page():
    st.empty()
    container = st.container()
    container.empty()
    container.image("home_trading_image.jpg", use_column_width=True)

    container.header("Welcome to the Multi-Page Stocks data Visualisation App!")
    container.subheader("Analyze and compare various stocks and indices with ease.")

    container.markdown("""
    This app allows you to explore various charts and comparisons related to stocks, indices, and cryptocurrencies. The app is divided into multiple pages, each with a specific focus:

    **1. Live Chart of New Zealand's Index** 🇳🇿
    * Observe the real-time performance of the New Zealand's index.

    **2. Companies' Stock Charts** 🏢
    * Line Chart: Visualize the stock price trends of a company.
    * Candlestick Chart: Analyze the stock price movement using candlestick patterns.
    * Volume Chart: Get insights into the trading volume of a company's stock.
    * Simple Moving Average (SMA) Chart: Observe the stock price's moving average for better trend analysis.
        * Simple Moving Averages (SMA) are widely used technical indicators in stock analysis to help identify trends and potential entry or exit points for trading. The SMA 50 and SMA 100 are two popular timeframes, referring to the 50-day and 100-day simple moving averages, respectively. They can be used to analyze a stock's performance in the following ways:
            * Identifying Trends: The direction and relative position of the SMA lines can help identify the overall trend of a stock. If the SMA 50 is above the SMA 100 and both are moving upwards, it suggests a bullish (upward) trend. Conversely, if the SMA 50 is below the SMA 100 and both are moving downwards, it indicates a bearish (downward) trend.
            * Signal for Entry or Exit: When the SMA 50 crosses above the SMA 100, it is considered a "golden cross," which is a bullish signal and could indicate a potential entry point for a long position. Conversely, when the SMA 50 crosses below the SMA 100, it is known as a "death cross," which is a bearish signal and could suggest a potential exit point or short entry.
            * Support and Resistance Levels: SMA lines can act as dynamic support or resistance levels. If the stock's price is above the SMA 50 and SMA 100, they can act as potential support levels. On the other hand, if the stock's price is below the SMA 50 and SMA 100, they can act as resistance levels.
            * Strength of Trend: The distance between the SMA 50 and SMA 100 can also provide insights into the strength of a trend. A larger gap between the two moving averages could indicate a strong trend, while a narrowing gap may suggest a weakening trend or potential trend reversal.
    * Relative Strength Index (RSI) Chart: Gauge the stock's momentum and potential price reversals.

    **3. Companies' Stock Comparison** 📊
    * Compare multiple companies' stocks in a single line chart.

    **4. Indices and Cryptocurrency Comparison** 🌐
    * Compare various indices with Bitcoin to analyze the correlation between the markets.


    **👈 Navigate to each page using the sidebar to explore these features. Happy analyzing!**
    """)

    container.markdown("⚠️ Disclaimer: The information provided on this app is for educational purposes only and should not be considered as financial advice.")

#home_page()