import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

day_df = pd.read_csv('https://raw.githubusercontent.com/hanakorui/Proyek-Akhir-Dicoding/master/Dashboard/Bike-sharing-dataset.%20csv/day.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/hanakorui/Proyek-Akhir-Dicoding/master/Dashboard/Bike-sharing-dataset.%20csv/hour.csv')

st.title("Bike Sharing Analysis :bike: :sparkles: ")

average_registered = day_df["registered"].mean()
average_temp = day_df["temp"].mean()

st.sidebar.title("Bike Sharing Analysis :bike:")
st.sidebar.write("Depends on")
side = st.sidebar.selectbox(
    label="Select data", options=("Day", "Hour"))

if side == "Day":
    st.subheader("What weather conditions lead to an increase in daily rental?")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Registered:", average_registered)
    with col2:
        st.metric("Average Temp:", average_temp)

    temp = day_df["temp"]
    register = day_df["registered"]

    fig_day, ax_day = plt.subplots(figsize=(10, 6))
    ax_day.scatter(temp, register, color="blue")
    ax_day.set_title("How Temperature Affects the Number of Registrants")
    ax_day.set_xlabel("Temp (Celcius)")
    ax_day.set_ylabel("Registered")
    ax_day.grid(color="gray")
    st.write(fig_day)

elif side == "Hour":
    st.subheader("How many registered bicycle users are there every hour under increasing weather conditions?")

    std_reg = hour_df["registered"].max()
    std_temp = hour_df["temp"].mean()
    avrg_hr = hour_df["hr"].max()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Most Registered: ", std_reg)
    with col2:
        st.metric("Hour: ", avrg_hr)
    with col3:
        st.metric("Temp: ", std_temp)

    temp = hour_df["temp"]
    register = hour_df["registered"]

    fig_hour, ax_hour = plt.subplots(figsize=(20, 10))
    ax_hour.scatter(temp, register, color="purple")
    ax_hour.set_title("How Temperature Affects the Number of Registrants")
    ax_hour.set_xlabel("Temp (Celcius)")
    ax_hour.set_ylabel("Registered")
    ax_hour.grid(color="gray")
    st.write(fig_hour)

st.caption("ratihranupadma")
