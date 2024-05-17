import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials
key_dict = json.loads(st.secrets["textkey"])
cred = credentials.Certificate(key_dict)
firebase_admin.initialize_app(cred)

