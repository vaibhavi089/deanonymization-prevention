import streamlit as st
import requests
import json

SERPER_API_KEY="564d47c4c1e9dd2035b95c628508c3e8702cb38b"
GEMINI_API_KEY="AIzaSyDFt1OpDYGXT8UCso_l2ikMA_ttzvAnTm0"


st.title("Trend Analysis Agent")
st.write("Enter a field of interst")

field = st.text_input("Enter a field of interest:", placeholder="data analyst")

def fetch_search_result(query):
    url="https://google.serper.dev/search"
    payload=json.dumps({
        "q" : query,
        "hl":"en"

    })

    headers={
        'X-API-KEY' : SERPER_API_KEY,
        'Content-Type' : 'application/json'
    }

    response = requests.post(url, headers=headers, data = payload)
    return response.json()

def generate_insights(text):
    url = 


