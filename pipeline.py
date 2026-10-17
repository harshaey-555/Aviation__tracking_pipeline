import pandas as pd
import os 
import requests
from datetime import datetime
import psycopg2
import sqlalchemy

DB_URL=     os.environ.get('NEON_DB_URL')


def flight_get_data():
    print("Fetching live flight data over India...")
    URL = "https://opensky-network.org/api/states/all?lamin=8.0&lomin=68.0&lamax=37.0&lomax=97.0"

    response=requests.get(URL)
    if response.status_code==200:
        data=response.json()
        states=data.get('states')

        if not states :
            print("No flights found in this bounding box right now.")
            return None

        columns = [
                    'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 
                    'longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 
                    'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 
                    'spi', 'position_source']
        df=pd.DataFrame(states,columns=columns)

        df = df[['callsign', 'origin_country', 'longitude', 'latitude', 'baro_altitude', 'velocity', 'on_ground']]

        df['callsign']= df['callsign'].str.strip()
        df['timestamp']= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df = df.dropna(subset=['longitude', 'latitude'])

        return df
    else :
        print(f"Failed with stautus code: {response.status_code()}")
        return None
flight_df= flight_get_data()
    
if flight_df is not None:
    print(f"\nSuccess! Found {len(flight_df)} flights.")
    print("\nSample Data:")
    print(flight_df.head())


    print("\nConnecting to postgreSQL...")
    engine = sqlalchemy.create_engine(DB_URL)
    flight_df.to_sql("live_flights", engine, if_exists="append", index=False)
    print("Success! Flight data inserted into the database.")

