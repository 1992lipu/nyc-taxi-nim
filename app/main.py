import duckdb
import folium
import pandas as pd
import streamlit as st
from openai import OpenAI
from streamlit_folium import folium_static

import sql_generator

conn = duckdb.connect(database=':memory:')
conn.execute("CREATE TABLE nyc_taxi_data AS SELECT * FROM 'data/train.csv'")

def query_data(query: str) -> pd.DataFrame:
    result = conn.execute(query).fetchdf()
    return result

def get_table_schema() -> pd.DataFrame:
    schema = conn.execute("PRAGMA table_info('nyc_taxi_data')").fetchdf()
    return schema

def generate_sql(user_query):
    client = OpenAI(
        base_url="http://localhost:5000/v1/chat/completions",
    )
    completion = client.chat.completions.create(
        model="nvidia/mistral-nemo-minitron-8b-8k-instruct",
        messages=[
            {"role": "system", "content": ""
                                          "Generate only the SQL query and nothing else. "
                                          "DO NOT ADD ANY COMMENTS OR DESCRIPTIONS. "
                                          "TABLE NAME IS 'nyc_taxi_data'"
                                          "SEND DUCKDB COMPATIBLE SQL QUERY"
                                          "TABLE HAS ONLY 2016 DATA"},
            {"role": "user",
             "content": f"Generate an SQL query with the following query: {user_query}, table schema is: {get_table_schema()}"}
        ],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return response

def query_taxi_data(sql_query):
    return query_data(sql_query)


st.title("NYC Taxi Data Explorer 🚖 with NVIDIA NIM")

# User query input
user_query = st.text_input("Ask a question about NYC Taxi Data:")

if user_query:
    sql_query = generate_sql(user_query)
    st.write("Generated SQL Query:", sql_query)

    if sql_query:
        df = query_taxi_data(sql_query)

        if not df.empty:
            # Map Visualization
            m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
            for _, row in df.iterrows():
                folium.Marker(
                    [row["pickup_latitude"], row["pickup_longitude"]],
                    popup=row["trip_duration"]
                ).add_to(m)

            folium_static(m)
        else:
            st.write("No data found for your query.")