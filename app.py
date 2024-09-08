import streamlit as st

page_1_signup = st.Page(
    page = "views/signup.py",
    title = "SignUp",
    icon = "🔑",
    default = True
)

page_2_login = st.Page(
    page = "views/login.py",
    title = "Login",
    icon = "🔐"
)

page_3_home = st.Page(
     page = "views/home.py",
    title = "Home",
    icon = "🏠"
)

page_4_newsapp = st.Page(
     page = "views/newsapp.py",
    title = "Taaza Khabhar",
    icon = "📃"
)

if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    pg = st.navigation(pages=[page_1_signup,page_2_login])
    pg.run()
else:
    pg = st.navigation(pages=[page_3_home,page_4_newsapp])
    pg.run()

