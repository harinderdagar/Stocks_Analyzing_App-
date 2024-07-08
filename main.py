# this is the main program of the app uses streamlit to control whole app
import streamlit as st
import welcome # Shows the welcome page of the app
import real_time_chart # Shows the real time chart
import stocks_charts # Shows various charts of a company
import compare_stocks # Shows the  various companies’ stocks performance comparison
import compare_bitcoin_indices #Shows the bitcoin and the indices's performance comparison

# Initialize session state for logged_in and current_page
def initialize_session_state():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

#Show the home page of the app
def show_home():
    st.session_state.current_page = "Home"
    st.header("Discover the Stocks App!!")
    st.write("Access the app by choosing Register or Login in the sidebar.")
    st.image("trading_image.jpg", use_column_width=True)

#Show the Register page of the app
def show_register():
    st.session_state.current_page = "Register"
    st.header("Register")
    username = st.text_input("Enter username:")
    password = st.text_input("Enter password:", type="password")
    password2 = st.text_input("Retype password:", type="password")

    if st.button("Submit"):
        result = auth_system.register(username, password, password2)
        if result == "Registration successful.":
            st.session_state.logged_in = True
            st.session_state.current_page = "Registration"
            st.experimental_rerun()
        else:
            st.warning(result)

#Show the Login page of the app
def show_login():
    st.session_state.current_page = "Login"
    st.header("Login")
    username = st.text_input("Enter username:")
    password = st.text_input("Enter password:", type="password")

    if st.button("Submit"):
        result = auth_system.login(username, password)
        if result == "Login successful.":
            st.session_state.logged_in = True
            st.session_state.current_page = "Welcome"
            st.empty()
            st.experimental_rerun()
        else:
            st.warning(result)


#Show the registration success message and exit button
def show_registration_success():
    st.header("Registration is successfull")
    st.write("Click on Exit button to go to main page")
    if st.button("Exit"):
        st.session_state.logged_in = False
        st.session_state.current_page = "Home"
        st.experimental_rerun()

#Show the Welcome page of the app after successful login
def show_welcome():
    st.empty()
    option = st.sidebar.selectbox(
        "Select the page from dropdown box:",
        ["Welcome", "Real_time_charts", "stocks_overview", "Compare_stocks", "Compare_bitcoin_indices", "logout"]
    )
    sidebar_multiselect_placeholder = st.sidebar.empty()
    sidebar_select_placeholder = st.sidebar.empty()
 
    # Display home page content after successful login
    if option == "Welcome":
        st.title('Stock analysing app')
        welcome.welcome_page()
        st.empty()
    # Display Companies' stock charts page
    elif option == "stocks_overview":
        st.title('Companies\' Stock performance overview and technical indicators charts')
        st.empty()
        stocks_charts.main(sidebar_select_placeholder)
        st.empty()
    # Display compare stocks performance page
    elif option == "Compare_stocks":
        st.title('Compare Companies\' Stocks')
        st.empty()
        compare_stocks.main(sidebar_multiselect_placeholder)
        st.empty()
    # Display compare bitcoin with indices page
    elif option == "Compare_bitcoin_indices":
        st.title('Compare bitcoin and major indices performance')
        st.empty()
        compare_bitcoin_indices.main(sidebar_multiselect_placeholder)
        st.empty()
    # Display real time charts page
    elif option == "Real_time_charts":
        st.title('Real time charts')
        st.empty()
        real_time_chart.main(sidebar_select_placeholder)
        st.empty()
    # Logout from the app
    elif option == "logout":
        st.session_state.logged_in = False
        st.session_state.current_page = "Home"
        st.warning('Logging Out')
#        st.experimental_rerun()
        # Redirect to specific URL
        redirect_url = "https://kubernetes-pro.com"  # Replace this with the URL you want to redirect to
        st.write(f'<meta http-equiv="refresh" content="0; URL={redirect_url}">', unsafe_allow_html=True)


# Main function of the app
def main():
    initialize_session_state()

    if not st.session_state.logged_in:
        show_welcome()

    elif st.session_state.current_page == "Registration":
        show_registration_success()

    elif st.session_state.current_page == "Welcome":
        show_welcome()

if __name__ == "__main__":
    main()
