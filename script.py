import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt



file = ('/Users/olisa/Downloads/clean_df.csv') # convert to websit link later
data = pd.read_csv(file)
data.head()


columns_to_drop = ['id', 'listing_url', 'description', 'neighborhood_overview', 'host_id', 'host_url', 'host_about', 'host_picture_url', 'host_verifications', 'host_identity_verified', 'neighbourhood_cleansed', 'bathrooms_text', 'amenities', 'first_review', 'last_review', 'instant_bookable']
data.drop(columns = columns_to_drop, inplace=True)
data.head()

data['price'] = pd.to_numeric(data['price'], errors ='coerce')
data_type = data['price'].dtype
data_type

# Create a Streamlit form
with st.form("filters_form"):
    st.header("Price Distribution Analysis")

    # Sidebar filters
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
    default_num_bedrooms = [1, 2, 3]  # Choose default values that exist in num_bedrooms
    selected_num_bedrooms = st.sidebar.multiselect(
    "Select Number of Bedrooms",
    options=num_bedrooms,
    default=default_num_bedrooms,
)

# Check if default values exist in options
    for value in default_num_bedrooms:
        if value not in num_bedrooms:
            st.error(f"Default value '{value}' does not exist in available options.")
            # Handle the error accordingly, e.g., provide a default value that exists in options or modify options.

    # Apply filters button
    submitted = st.form_submit_button("Apply Filters")  # This line is now inside the form block

# Apply filters if the form is submitted
if submitted:
    filtered_data = data.query(
        "price >= @price_min & price <= @price_max & property_type in @selected_property_types & room_type in @selected_room_types & bedrooms in @selected_num_bedrooms"
    )

    # Visualizations
    st.subheader("Price Distribution")
    fig, ax = plt.subplots()
    ax.hist(filtered_data["price"], bins=20, edgecolor='black')
    ax.set_xlabel("Price")
    ax.set_ylabel("Count")
    ax.set_title("Price Distribution Histogram")
    st.pyplot(fig)

    st.subheader("Price vs Bedrooms Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(filtered_data["bedrooms"], filtered_data["price"])
    ax.set_xlabel("Number of Bedrooms")
    ax.set_ylabel("Price")
    ax.set_title("Price vs Bedrooms Scatter Plot")
    st.pyplot(fig)

    # Metrics
    st.subheader("Price Metrics")
    st.write(f"Total Listings: {len(filtered_data)}")
    st.write(f"Average Price: ${filtered_data['price'].mean():.2f}")
    st.write(f"Median Price: ${filtered_data['price'].median():.2f}")
    st.write(f"Price Range: ${filtered_data['price'].min():.2f} - ${filtered_data['price'].max():.2f}")
    st.write(filtered_data.groupby('property_type')['price'].mean())


