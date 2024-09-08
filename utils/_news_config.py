import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("MEDIA_STACK_NEWS_API")

def display_news(country, category, lang, apikey):
    url = 'http://api.mediastack.com/v1/news'
    
    params = {
        'access_key': '{}'.format(apikey),
        'categories': '{}'.format(category.lower()),
        'countries': '{}'.format(country),
        'languages': '{}'.format(lang),
        'sort': 'popularity',
        'limit': 40
    }    

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        news_items = data.get("data", [])
        
        # print(news_items)
        
        if news_items:
            for item in news_items:

                title = item.get("title", "No Title")
                image = item.get("image", "")
                description = item.get("description", "No description available.")
                news_url = item.get("url", "No url")
                source = item.get("source", "Unknown Source")
                country = item.get("country", "Unknown Country")
                published_at = item.get("published_at", "").split('T')[0]
                
                # print(image)
                
                if image and not image.startswith("http"):
                    image = "https:" + image.split(":")[1]

                container_html = f"""
                    <br>
                    <div style="border: 6px solid red; padding: 10px; border-radius: 20px;">
                    <h3>{title}</h3>
                    <hr style="border:3px solid red;">
                    <img src="{image if image else 'https://via.placeholder.com/150'}" alt="Sample image" style="width:100%; max-width:800px;"/>
                    <h4>{description}</h4>
                    <h5>For more information click on the below link :</h5>
                    <h5><a href="{news_url}">Click me!</a></h5>
                    <h5>Source: {source.title()}</h5>
                    <h5>Country: {country.title()}</h5>
                    <h5>Published at: {published_at}</h5>
                    <hr style="border:3px solid red;">
                    </div>
                    <br>
                """

                st.markdown(container_html, unsafe_allow_html=True)
        else:
            st.error("No articles found.")
        
    elif response.status_code >= 500 and response.status_code <= 510:
        st.error(f"Failed To Fetch News : {response.status_code} - {response.reason}")

# display_news("in","health","en", apikey)