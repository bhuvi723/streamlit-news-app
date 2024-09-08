import streamlit as st
from utils._db_operations import verify_login
import time

def show_login():
    st.title(":red[TAAZA KHABHAR] : The Trending News App.")
    st.markdown('<hr style="border-top: 2px solid red;">',unsafe_allow_html=True)

    with st.container():
        st.header("Login :")
        name = st.text_input("name :")
        password = st.text_input("Password :", type="password")
        if st.button("Login"):
            if not name:
                st.warning("enter the name 😒!")
                st.stop()
                
            if not password:
                st.warning("enter the password 🤔!")
                st.stop()
            
            if verify_login(name,password) == True:
                st.session_state['logged_in'] = True
                st.session_state['user_name'] = name
                st.success("login successfull 🤩!")
                st.write("redirecting........")
                # redirect to the home page!
                time.sleep(2)
                st.rerun()
            elif verify_login(name,password) == "unable to verify!":
                st.error("unable to verify the login details!")
                st.stop()
            else:
                st.error("recheck the details 😣!")
                st.stop()

        else:
            st.write("<h5>Don't have an account ?</h5>",unsafe_allow_html=True)
            if st.button("click me"):
                st.switch_page("views/signup.py")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False  
    
if st.session_state['logged_in']:
    # If logged in, redirect to home
    st.switch_page("views/home.py")
else:
    show_login()