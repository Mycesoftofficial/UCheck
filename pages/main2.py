import pandas as pd
import streamlit as st
import plotly_express as px


#____Main Page____
st.title(":bar_chart: Staff Monitoring  Data Form")
st.caption(" Rating: EXCELLENT = 5, GOOD  = 4, SATISFACTORY = 3, NEEDS IMPROVEMENT = 2, UNSATISFACTORY = 1")

tab1, tab2, tab3, tab4 = st.tabs(["ACADEMICS ", "DOMESTICS", "TRANSPORT", "COMPLAINS"])

with tab1:
    with st.form(key="email_forms"):
        User_Full_Name = st.text_input("Please enter your Full Name")
        User_Contact = st.text_input("Phone Number (Must be Whatsapp Number)")
        ResidentialLoc = st.text_input(
            "State the Area you stay. Example (Nyanyano -Teachers Quarters). This makes it very easy for Employers to select you based on your closeness to the school.")


        button = st.form_submit_button()

