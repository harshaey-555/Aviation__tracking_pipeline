import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os

# --- Page Configuration ---
st.set_page_config(page_title="Live Aviation Tracker", page_icon="✈️", layout="wide")


DB_URL = st.secrets["NEON_DB_URL"]


@st.cache_data(ttl=600)  
def load_data():
    engine = create_engine(DB_URL)
    
    query = "SELECT * FROM live_flights"
    df = pd.read_sql(query, engine)
    return df

st.title("✈️ Live Aviation Tracker - India Airspace")
st.markdown("Real-time flight geospatial data extracted via OpenSky API and automated with GitHub Actions.")

df = load_data()

if df.empty:
    st.warning("No flight data found in the database. Wait for the pipeline to run!")
else:
    # --- Data Filtering ---
    # The database holds historical data. We only want to plot the most recent snapshot on the map.
    latest_timestamp = df['timestamp'].max()
    current_flights = df[df['timestamp'] == latest_timestamp]
    
    # --- Top Metrics ---
    airborne_count = len(current_flights[current_flights['on_ground'] == False])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Latest Data Snapshot", latest_timestamp)
    col2.metric("Total Flights Tracked", len(current_flights))
    col3.metric("Currently Airborne", airborne_count)
    
    st.divider()

    # --- Interactive Plotly Map ---
    st.subheader("Live Flight Map")
    
    # Create a scatter mapbox plot
    fig = px.scatter_map(
        current_flights, 
        lat="latitude", 
        lon="longitude", 
        hover_name="callsign", 
        hover_data={"origin_country": True, "velocity": True, "baro_altitude": True, "latitude": False, "longitude": False},
        color="velocity",  # Color the planes by how fast they are going
        color_continuous_scale=px.colors.sequential.Plasma,
        zoom=3.5, 
        height=600
    )
    
    # Set the map style (carto-positron is a clean, free basemap)
    fig.update_layout(map_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    st.plotly_chart(fig, use_container_width=True)

    # --- Raw Data Table ---
    with st.expander("View Raw Flight Data"):
        st.dataframe(current_flights)