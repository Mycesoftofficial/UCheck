import pandas as pd
import streamlit as st
import plotly_express as px





#st.set_page_config(page_title="Staff Monitoring System",
                   #layout="wide"
#)

df = pd.read_excel(
    io='kempshotSMS.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    nrows=10

)

#st.dataframe(df)

#codes for the side navigation bar
st.sidebar.caption("Home")
st.sidebar.subheader("Search")
Month = st.sidebar.multiselect("Select Month:",
                                options=df["Month"].unique(),
                                )

Term = st.sidebar.multiselect("Select Term:",
                                options=df["Term"].unique(),

                                )
Department = st.sidebar.multiselect("Select Department:",
                                options=df["Department"].unique(),
                                #default=df["Department"].unique()
                                )

StaffName = st.sidebar.multiselect("Select Staff Name:",
                                options=df["StaffName"].unique(),
                                #default=df["StaffName"].unique()
                                )


#Executing the Search Query
df_selection = df.query(
    #"Month == @Month & StaffName == @StaffName & Term == @Term & Department == @Department "
    "Department == @Department & StaffName == @StaffName & Term == @Term & Month == @Month"
)
#____Main Page____
st.title(":bar_chart: Staff Monitoring Dashboard ")

#st.dataframe(df_selection)
st.markdown("##")


#Coding the KPI parts for the data
Work_Reporting_Time = round(df_selection["Work Reporting Time"].mean(), 2)
Morning_At_Post = round(df_selection["Morning At Post"].mean(), 2)
Grounds_Work = round(df_selection["Gworks"].mean(), 2)
Silence_Hour = round(df_selection["Shours"].mean(), 2)
Assembly = round(df_selection["Assembly"].mean(), 2)
Punctuality = round(df_selection["Punctuality"].mean(), 2)
Hwmarked = round(df_selection["Homeworkmarked"].mean(), 2)
Middaypost = round(df_selection["Middaypost"].mean(), 2)

Workoutput = round(df_selection["Workoutput"].mean(), 2)
Hwcorrecton = round(df_selection["Hwcorrection"].mean(), 2)
Pquality = round(df_selection["Pquality"].mean(), 2)
Wleg = round(df_selection["wlegibly"].mean(), 2)
Clsmgt = round(df_selection["clsmgt"].mean(), 2)



Querypoints = round(df_selection["Querypoints"].mean(), 2)



tab1, tab2 = st.tabs(["Instructional Time ", "Query Records"])


with tab1.caption("Sales By Percentiles"):
    st.subheader('Rating ')
    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
    with c1:
        st.info('Reporting Att')
        st.subheader(Work_Reporting_Time)
        st.markdown("___")

    with c2:
        st.info("Morning Post")
        st.subheader(Morning_At_Post)
        st.markdown("___")

    with c3:
        st.info('GroundsWork')
        st.subheader(Grounds_Work)
        st.markdown("___")

    with c4:
        st.info('Silence Hour')
        st.subheader(Silence_Hour)
        st.markdown("___")

    with c5:
        st.info('Assembly')
        st.subheader(Assembly)
        st.markdown("___")

    with c6:
        st.info('Punctuality')
        st.subheader(Punctuality)
        st.markdown("___")

    with c7:
        st.info('HW Marked')
        st.subheader(Hwmarked)
        st.markdown("___")

    with c8:
        st.info('Midday Post')
        st.subheader(Middaypost)
        st.markdown("___")

st.markdown("##")
st.text(":bar_chart: Staff Monitoring App")

with c1:
    st.info('WorkOutput')
    st.subheader(Workoutput)
    st.markdown("___")

with c2:
    st.info('HW Corrtn.')
    st.subheader(Hwcorrecton)
    st.markdown("___")

with c3:
    st.info('P Quality.')
    st.subheader(Pquality)
    st.markdown("___")

with c4:
    st.info('W. legibility')
    st.subheader(Wleg)
    st.markdown("___")

with c5:
    st.info('Class Mgt')
    st.subheader(Clsmgt)
    st.markdown("___")

st.markdown("##")
st.text(":bar_chart: Staff Monitoring App")


with tab2:
     st.subheader(Querypoints)
        #st.subheader(Clsmgt)
     st.caption(" Rating: EXCELLENT = 5, GOOD  = 4, SATISFACTORY = 3, NEEDS IMPROVEMENT = 2, UNSATISFACTORY = 1")
     df_selection.drop(columns=['Check Time 1', 'Work Reporting Time', 'Morning At Post', 'Gworks', 'Shours', 'Assembly', 'Punctuality', 'Homeworkmarked', 'CheckTime 2', 'Middaypost', 'Workoutput', 'Hwcorrection', 'Pquality', 'wlegibly', 'Check Time 3', 'clsmgt', 'Pupilneatness', 'Workattitude', 'Teachingpreparation', 'Check Time 4', 'Homeworkgiven', 'Attregister', 'Classcleaning', 'Meetingdeadlines', 'Weeklymock', 'Totals'], inplace=True)
     st.table(df_selection)





#hiding the streamlit features
hide_St_Style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_St_Style, unsafe_allow_html=True)
            
