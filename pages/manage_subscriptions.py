import streamlit as st
import json

with open('subscriptions.json', 'r') as f:
    subscriptions = json.load(f)


st.set_page_config(layout='wide')

st.header('Manage subscriptions')

content = """
Here you can remove or edit your subscriptions.\n
"""
st.write(content)

def edit():
    remove()
    user_email = st.session_state.get('user_email')
    new_topic = st.session_state['new_topic']
    subscriptions[user_email].append(new_topic)

def remove():
    user_email = st.session_state.get('user_email')
    for topic in subscriptions[user_email]:
        if st.session_state[topic]:
            subscriptions[user_email].remove(topic)

user_mail = st.text_input('Your email adress:', key='user_email')
show_buton = st.button('View subscriptions', key='view')
if show_buton or user_mail:
    user_email = st.session_state.get('user_email')
    if user_email:
        if not user_email in subscriptions.keys():
            response = """
            Sorry, you are not subscribed yet, pleas go back to main page and add
            your email with a topic you are interested in.
            """
            st.write(response)
        else:
            st.write("Your subscriptions:")
            checkbox_sum = 0
            for topic in subscriptions[user_email]:
                checkbox = st.checkbox(topic, key=topic)
                checkbox_sum += checkbox
            
            if checkbox_sum == 1:
                st.text_input(label='New topic', key='new_topic')
                col1, col2 = st.columns(2)
                with col1:
                    st.button(label='Edit', key='edit', on_click=edit)
                with col2:
                    st.button(label='Remove', key='remove', on_click=remove)
            elif checkbox_sum > 1:
                st.button(label='Remove', key='remove', on_click=remove)
    else:
        st.write("Please provide your email adress in order to view subscriptions")


