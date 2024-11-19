import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configure the app
st.set_page_config(
    page_title="NFL 2003-2023 TEAM STATS",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data from Google Sheets
gsheetid = '1Q0IkCu7Z58kENRbpsTVAigQnlNZUpchVgA6zfgmh2Xw'
sheetid = '1680457813'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheetid}'
df = pd.read_csv(url)

# Encode teams and clean data
# Dictionary for encoding NFL teams as numbers
nfl_teams_dict = {
    "Arizona Cardinals": 1,
    "Atlanta Falcons": 2,
    "Baltimore Ravens": 3,
    "Buffalo Bills": 4,
    "Carolina Panthers": 5,
    "Chicago Bears": 6,
    "Cincinnati Bengals": 7,
    "Cleveland Browns": 8,
    "Dallas Cowboys": 9,
    "Denver Broncos": 10,
    "Detroit Lions": 11,
    "Green Bay Packers": 12,
    "Houston Texans": 13,
    "Indianapolis Colts": 14,
    "Jacksonville Jaguars": 15,
    "Kansas City Chiefs": 16,
    "Las Vegas Raiders": 17,
    "Los Angeles Chargers": 18,
    "Los Angeles Rams": 19,
    "Miami Dolphins": 20,
    "Minnesota Vikings": 21,
    "New England Patriots": 22,
    "New Orleans Saints": 23,
    "New York Giants": 24,
    "New York Jets": 25,
    "Oakland Raiders": 26,
    "Philadelphia Eagles": 27,
    "Pittsburgh Steelers": 28,
    "San Diego Chargers": 29,
    "San Francisco 49ers": 30,
    "Seattle Seahawks": 31,
    "St. Louis Rams": 32,
    "Tampa Bay Buccaneers": 33,
    "Tennessee Titans": 34,
    "Washington Commanders": 35,
    "Washington Football Team": 36,
    "Washington Redskins": 37
    
}

# Sidebar menu for navigation
menu = ["Home", "Statistics", "Visualization"]
choice = st.sidebar.selectbox("Navigation", menu)

# CSS
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f2f6;
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #3949ab;
        color: white;
    }
    h1, h2, h3 {
        color: #427BD6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home Page
if choice == "Home":
    st.title("🏈 NFL 2003-2023 TEAM STATS")
    st.write("Welcome to the NFL Team Stats mini site! Use the sidebar to navigate through sections.")
    st.dataframe(df, use_container_width=True)

# Statistics Page
elif choice == "Statistics":
    st.title("📊 Team Statistics")

    # Display basic statistics of numeric columns
    st.write("### Descriptive Statistics")
    st.write(df.describe())

    # Calculate mean values for each team
    team_stats = df.groupby("team")[["wins", "losses", "points", "total_yards"]].mean().reset_index()

    # Display the table of mean values
    st.write("### Mean Wins, Losses, Points, and Total Yards by Team")
    st.table(team_stats)

# Visualizations Page
elif choice == "Visualizations":
    st.title("📈 Team Visualizations")
    st.write("Visualization of every team wins from 2003-2023")
    fig = px.bar(df, x="team", y="wins")
    st.plotly_chart(fig)
