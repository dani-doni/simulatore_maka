# streamlit_app.py

import streamlit as st
import json
key_dict = json.loads(st.secrets["firestore"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="maka")

performance = db.collection("performance")

for p in performance.stream():
	st.write("The start is: ", p.start)
	st.write("The finish is: ", p.finish)
