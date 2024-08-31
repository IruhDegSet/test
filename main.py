import streamlit as st

with open('db.txt', 'r+') as f:
    db= f.read().split('\n')

query= st.chat_input('say something')
if query:
    db.append(query)
    with open('db.txt', 'a') as f:
        f.write(f'{query}\n')

for msg in db:
    st.write(msg)