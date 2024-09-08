import streamlit as st
import os
import requests
from utils._news_config import display_news
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("MEDIA_STACK_NEWS_API")

def show_news_app():
    st.set_page_config(page_title="Taaza Khabhar: News App", page_icon=":newspaper:")

    st.title(":red[TAAZA KHABHAR] :")
    col1, col2 = st.columns([8,2],gap="small",vertical_alignment="bottom")
    with col1:
        st.subheader("**The Trending News App**")
    with col2:
        # st.write('**Hi, {}**'.format(st.session_state['user_name']))
        st.write('<p style="font-size: 19px; font-weight: bold;">Hi✋, {}.</p>'.format(st.session_state['user_name'].title()),unsafe_allow_html=True)
    
    st.markdown('<hr style="border:1px solid red;">', unsafe_allow_html=True)

    st.sidebar.title(":red[**NEWS :**]")

    country = st.sidebar.selectbox(
        ":red[Choose The Country: ]",
        ['India', "Australia", "Germany", "United States"]
    )

    countries = {
        "India": "in",
        "Australia": "au",
        "Germany": "de",
        "United States": "us"
    }

    category = st.sidebar.selectbox(
        ':red[Choose the News Category: ]',
        ['Sports', 'Business', 'Health', 'Technology', 'Entertainment', 'Science']
    )

    lang = st.sidebar.radio(
        ":red[Choose The Language : ]",
        ("English", "French", "Dutch", "Russian")
    )

    languages = {
        "English": "en",
        "French": "fr",
        "Dutch": "nl",
        "Russian": "ru"
    }

    country_selected = countries[country]
    language_selected = languages[lang]

    if language_selected and country_selected and category and country:
        col1, col2, col3 = st.columns([8,0.5,1.5],vertical_alignment="bottom")
        with col1:
                st.markdown(f'''<h2><b style="color: red;">Here is your </b><b>{country}\'s {category} news!</b></h2>''',unsafe_allow_html = True)
        with col3:
            if st.button("log out"):
                st.session_state['logged_in'] = False
                st.session_state['user_name'] = None
                st.rerun()
        display_news(country_selected, category, language_selected, apikey)
    else:
        st.warning("Enter necessary details!")


if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = False
    
if st.session_state['logged_in']:
    show_news_app()
else:
    st.switch_page("views/login.py")