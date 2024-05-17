import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Load the JSON key from secrets
key_dict = json.loads(st.secrets["textkey"])

# Initialize Firebase Admin SDK
cred = credentials.Certificate(key_dict)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Access Firestore database
db = firestore.client()

# Example function to fetch data from Firestore
def fetch_data_from_firestore(collection_name):
    docs = db.collection(collection_name).stream()
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    return data

# Streamlit app code
st.title("Firebase Firestore Data")
collection_name = st.text_input("Enter Firestore collection name", "your-collection-name")

if st.button("Fetch Data"):
    data = fetch_data_from_firestore(collection_name)
    st.write(data)




