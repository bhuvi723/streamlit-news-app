import streamlit as st
import re
from  utils._db_operations import authenticate_user, insert_user, create_table, is_conn
import uuid
import time

st.title(":red[TAAZA KHABHAR] : The Trending News App.")

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False

with st.container():
    st.markdown('<hr style="border-top: 2px solid red;">',unsafe_allow_html = True)
    st.header("SignUp :") 
    
    name = st.text_input("User Name :")
    email = st.text_input("Email :")
    password = st.text_input("Password :",type="password")
    confirm_password = st.text_input("Confirm Password :",type="password")
    
    if st.button("Sign in"):
        
        if not name:
            st.warning("enter the name 😫!")
            st.stop()
        
        if not email:
            st.warning("enter the email 😒!")
            st.stop()
            
        if not is_valid_email(email):
            st.error("enter valid email address 🤔!")
            st.stop()
            
        if password == confirm_password:
            
            if is_conn():
                create_table("users")
                if authenticate_user(name,password) == True:
                    st.error("user already exists!")
                    st.stop()
                # elif authenticate_user(name,password) == "unable to authenticate!":
                #     st.error("unable to authenticate!")
                #     st.stop()
                else:
                    # create_table("users")
                    uid = uuid.uuid4().hex
                    insert_user(uid,name,email,password)
                    st.success("sign-in successfull 🤩!")
                    st.write("redirecting...")
                    time.sleep(2)
                    st.switch_page("views/login.py")
                    # redirect to the login page - optional
            else:
                st.warning("If you have account login! otherwise")
                st.error("There Is Somthing Wrong Come Back Later")
        else:
            st.error("passwords donot match 🤨!")
            st.stop()


    st.markdown("<h5>Already have an account?</h5>",unsafe_allow_html=True)
    if st.button("click me"):
        st.switch_page("views/login.py")