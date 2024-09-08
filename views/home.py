import streamlit as st

def show_home():
    st.title(":red[TAAZA KHABHAR] : The Trending News App.")
    st.write('<p style="font-size: 19px; font-weight: bold;">Hi✋, {}.</p><hr style="border-top: 2px solid red;">'.format(st.session_state['user_name'].title()),unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([6.5,3.5],gap="small",vertical_alignment="top")
        with col1:
            st.markdown('''
                    <ul type="circle">
                        <li style="font-size: 20px;">
                            Taaza Khabhar is a trending web app designed to seamlessly deliver news 
                            across multiple countries, covering diverse 
                            categories like business, sports, health, technology, and more.
                        </li>
                        <li style="font-size: 20px;">
                            It supports various languages, including English, French, Dutch, 
                            Russian, and others, ensuring accessibility for a global audience.
                        </li>
                    </ul>''',unsafe_allow_html=True)
            
        with col2:
            st.image("images/th_home.jpeg")
                    
        st.markdown('''<ul type="circle">
                <li style="font-size: 20px;">
                    With a user-friendly, attractive, and simple interface, Taaza Khabhar 
                    provides a smooth and engaging experience for users. 
                    Built with strong encryption, the app prioritizes the security and 
                    privacy of user data, making it a reliable platform for staying informed 
                    on the latest news.
                </li>
            </ul>''',unsafe_allow_html=True)
            
        # if st.button("go to app"):
        #     st.switch_page("pages/newsapp.py")
            
        col1, col2, col3, col4, col5 = st.columns([1.5,2,2,2,1.5])
        
        with col1:
            if st.button("go to app"):
                st.switch_page("views/newsapp.py")
            
        with col5:
            if st.button("log out"):
                st.session_state['logged_in'] = False
                st.session_state["user_name"] = None
                st.rerun()
            

if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = False
    
if st.session_state['logged_in']:
    show_home()
else:
    st.switch_page("views/login.py")