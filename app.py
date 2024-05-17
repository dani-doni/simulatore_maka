# streamlit_app.py

import streamlit as st

# Create a connection object.
conn = st.connection("firestore")
conn

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(conn)
firebase_admin.initialize_app(cred)
