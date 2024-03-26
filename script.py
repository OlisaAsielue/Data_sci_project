import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import geopandas as gpd


# Reading data into notebook
file = ('/Users/olisa/Downloads/clean_df.csv') # convert to websit link later
data = pd.read_csv(file)
data.head()

# Start of data cleaning process. Dropping the columms not needed
columns_to_drop = ['id', 'listing_url', 'description', 'neighborhood_overview', 'host_id', 'host_url', 'host_about', 'host_picture_url', 'host_verifications', 'host_identity_verified', 'neighbourhood_cleansed', 'bathrooms_text', 'amenities', 'first_review', 'last_review', 'instant_bookable']
data.drop(columns = columns_to_drop, inplace=True)
data.head()

# Converting to the right data type
data['price'] = pd.to_numeric(data['price'], errors ='coerce')
data_type = data['price'].dtype
data_type

# Handle missing values in the 'price' column
data['price'] = data['price'].fillna(data['price'].mean())
data_type = data['price'].dtype
print(data_type)

# Calculate 'reviews_per_month' and handle missing values in 'number_of_reviews' and 'listing_days' columns
data['reviews_per_month'] = np.where(data['number_of_reviews'].isnull(), 0, data['number_of_reviews'] / data['listing_days'] * 30)

# Handle missing values in 'number_of_reviews' and 'listing_days' columns
data['number_of_reviews'] = data['number_of_reviews'].fillna(data['number_of_reviews'].mean())
data['listing_days'] = data['listing_days'].fillna(data['listing_days'].mean())



