import streamlit as st
import json

with open('subscriptions.json', 'r') as f:
    subscriptions = json.load(f)

st.set_page_config(layout='wide')

st.header('Unsubscribe')

content = """
Here you can provide your email adress in order to remove it from our database.\n
"""
st.write(content)


with st.form(key='email_form'):
    user_email = st.text_input('Your email adress:')

    submit_button = st.form_submit_button('Subscribe')
    if submit_button:
        if user_email in subscriptions.keys():
            del subscriptions[user_email]
            with open('subscriptions.json', 'w') as f:
                json.dump(subscriptions, f, indent=4)

        st.info("Your subscribtion was removed successfully")

