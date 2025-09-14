import streamlit as st
import pandas as pd

st.title("AI-Driven Threat Detection Dashboard")

alerts = pd.read_csv('data/ai_alerts.csv')

st.header("Recent Alerts")
st.dataframe(alerts[['alert', 'packet_size', 'duration', 'protocol']])

st.header("Alert Distribution by Protocol")
st.bar_chart(alerts['protocol'].value_counts())
