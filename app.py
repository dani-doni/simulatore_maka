import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
key_dict = json.loads(st.secrets["textkey"])
cred = credentials.Certificate(key_dict)
db = firestore.Client(credentials=cred, project="maka")



