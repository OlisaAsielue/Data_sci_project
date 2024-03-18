import pandas as pd
import numpy as np
import streamlit as st


file = ('/Users/olisa/Downloads/clean_df.csv') # convert to websit link later
data = pd.read_csv(file)
data.head()


columns_to_drop = ['id', 'listing_url', 'description', 'neighborhood_overview', 'host_id', 'host_url', 'host_about', 'host_picture_url', 'host_verifications', 'host_identity_verified', 'neighbourhood_cleansed', 'bathrooms_text', 'amenities', 'first_review', 'last_review', 'instant_bookable']
data.drop(columns = columns_to_drop, inplace=True)
data.head()

data['price'] = pd.to_numeric(data['price'], errors ='coerce')
data_type = data['price'].dtype
data_type

# Sidebar Header
st.sidebar.header("Filters")

# Price Range Slider
price_min, price_max = st.sidebar.slider(
    "Select Price Range",
    min_value=0.0,
    max_value=float(data["price"].max()),
    value=(0.0, float(data["price"].max())),
    step=10.0,
)

# Property Type Filter
property_types = data["property_type"].unique()
selected_property_types = st.sidebar.multiselect(
    "Select Property Types",
    options=property_types,
    default=property_types,
)

# Room Type Filter
room_types = data["room_type"].unique()
selected_room_types = st.sidebar.multiselect(
    "Select Room Types",
    options=room_types,
    default=room_types,
)

# Number of Bedrooms Filter
num_bedrooms = data["bedrooms"].unique()
selected_num_bedrooms = st.sidebar.multiselect(
    "Select Number of Bedrooms",
    options=num_bedrooms,
    default=num_bedrooms,
)

# Apply filters
filtered_data = data.query(
    "price >= @price_min & price <= @price_max & property_type in @selected_property_types & room_type in @selected_room_types & bedrooms in @selected_num_bedrooms"
)