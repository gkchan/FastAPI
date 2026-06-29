import requests
import streamlit as st

# Command to start the server: streamlit run frontend_streamlit.py 
# URL to view the frontend: http://localhost:8501

st.title("FastAPI Streamlit Frontend")

if st.button('Check health'):
    with st.spinner('Checking health...'):
        backend_url = "http://localhost:8000/health"
        try:
            response = requests.get(backend_url)
            if response.status_code == 200:
                st.success("Service is healthy!")
            else:
                st.error(f"Service is not healthy. Status code: {response.status_code}")
            st.write(response.json())
        except requests.RequestException as e:
            st.error(f"Error occurred while checking health: {e}")

text = st.text_input("Enter text here:")

num = st.number_input("Enter a number:", step=1, value=0)

date = st.date_input("Select a date:")