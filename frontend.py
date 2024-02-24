import streamlit as st
import requests

# Streamlit form for user input
st.title('Data Submission Form')

with st.form("user_data_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    transfer_limit = st.number_input("Transfer Limit", min_value=0.0, format='%f')
    nid = st.text_input("National ID")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "transfer_limit": transfer_limit,
            "nid": nid
        }
        headers = {'x-password': 'c2eab9ef017e81b9e2799f44824b7974697f72919d14dca6b4e68e8a7a6f5195'}
        
        response = requests.post("https://sarab-project.onrender.com/process-data/", json=data, headers=headers)
        if response.status_code == 200:
            result_data = response.json()
            st.success("Data Processed Successfully!")
            st.write(result_data)
        else:
            st.error(f"An error occurred: {response.json()}")