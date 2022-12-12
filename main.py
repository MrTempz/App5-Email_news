import streamlit as st
import json


with open('subscriptions.json', 'r') as f:
    subscriptions = json.load(f)

st.set_page_config(layout='wide')

st.title("Email  News!")

content = """
Here you can provide your email adress and topics you are interested in.\n
You will receive an email daily containing news regarding the topics you are 
interested in.\n
You can always change your interests in "manage subscriptions" tab,
or unsubscribe in "unsubscribe" tab.
"""
st.write(content)


with st.form(key='email_form'):
    user_email = st.text_input('Your email adress:')
    topic = st.text_input('Topic you are interested in:')

    submit_button = st.form_submit_button('Subscribe')
    if submit_button:
        user_subscriptions = subscriptions.get(user_email, [])
        user_subscriptions.append(topic)
        user_subscriptions = list(set(user_subscriptions))

        subscriptions[user_email] = user_subscriptions
        with open('subscriptions.json', 'w') as f:
            json.dump(subscriptions, f, indent=4)

        st.info("Your subscribtion was added successfully")

