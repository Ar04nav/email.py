import streamlit as st
st.title("Feedback Form")
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
submitted = st.form_submit_button("Submit Feedback")
if submitted:
    st.success(f"Thank you,{name}, for your feedback!") 
