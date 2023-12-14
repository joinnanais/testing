# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import altair as alt
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
from urllib.error import URLError

st.set_page_config(
        page_title="Sales Dashboard",
        page_icon=":bar_chart:",
        layout = "wide",
        menu_items={
        'Get Help': "https://uk.elemis.com/featured/special-promotion?gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh2MCbFg-Fckqjejakv8MtT7BI4D9ggNA1dKUYcC4BB4AE3CVWaqpVsaAuAqEALw_wcB",
        'Report a bug': "https://uk.elemis.com/featured/special-promotion?gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh2MCbFg-Fckqjejakv8MtT7BI4D9ggNA1dKUYcC4BB4AE3CVWaqpVsaAuAqEALw_wcB",
        'About': "# This app is designed for CDP prototype - this is a test dashboard"}
        )

st.markdown(
        """
        # Sales Dashboard :bar_chart:

        This is a prototype dashboard to demonstrate the concept of Streamlit for CDP purposes.
        

        The data is from an open-source.
        
        
        The data used is a superstore sample data from Kaggle which contains sales and profit.
        """
    )

github_csv_url = 'https://raw.githubusercontent.com/joinnanais/Elemis/main/Sample%20-%20Superstore.csv'
data = pd.read_csv(github_csv_url, encoding='latin1')
df = pd.DataFrame(data)

# Calculate average sales and profit
average_sales = round(df['Sales'].mean(), 2)
average_profit = round(df['Profit'].mean(), 2)
average_quantity = round(df['Quantity'].mean(), 0)

# Display KPIs side by side
st.title('Key Performance Indicators (KPIs)')

# Create a two-column layout
col1, col2, col3 = st.columns(3)

# Display Average Sales in the first column
with col1:
    st.subheader('Average Sales:')
    st.metric(label='$', value=average_sales, delta=None)

# Display Average Profit in the second column
with col2:
    st.subheader('Average Profit:')
    st.metric(label='$', value=average_profit, delta=None)

with col3:
    st.subheader('Average Quantity of Sales:')
    st.metric(label='X', value=average_quantity, delta=None)

st.sidebar.header("Filters")

# Add a slider for discount
st.header('Discount Slider')
discount_range = st.slider('Select Discount Range', min_value=0.0, max_value=1.0, step=0.01, value=(0.0, 0.2))

# Select category filter
category_filter = st.sidebar.multiselect("Select Category", df['Category'].unique(), df['Category'].unique())

# Select sub-category filter
sub_category_filter = st.sidebar.multiselect("Select Sub-Category", df['Sub-Category'].unique(), df['Sub-Category'].unique())

# Select city filter
city_filter = st.sidebar.multiselect("Select City", df['City'].unique(), df['City'].unique())

# Select Region
region_filter = st.sidebar.multiselect("Select Region", df['Region'].unique(), df['Region'].unique())

# Select Product Name
product_filter = st.sidebar.multiselect("Select Product Name", df['Product Name'].unique(), df['Product Name'].unique())

# Select Segment 
segment_filter = st.sidebar.multiselect("Select Segment", df['Segment'].unique(), df['Segment'].unique())

# Date Filter
# Date range slider
# Convert dates 

# Convert 'Order Date' to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Streamlit app
st.title('Filter by Order Date')

# Set default values within the range of the data
default_start_date = df['Order Date'].min().date()
default_end_date = df['Order Date'].max().date()

# Date range slider with default values
start_date = st.date_input('Start Date', default_start_date, min_value=df['Order Date'].min().date(), max_value=df['Order Date'].max().date())
end_date = st.date_input('End Date', default_end_date, min_value=df['Order Date'].min().date(), max_value=df['Order Date'].max().date())

filtered_df = df[(df['Category'].isin(category_filter)) & 
                 (df['Sub-Category'].isin(sub_category_filter)) &
                 (df['City'].isin(city_filter)) &
                 (df['Region'].isin(region_filter)) &
                 (df['Product Name'].isin(product_filter)) &
                 (df['Segment'].isin(segment_filter)) &
                 (df['Order Date'] >= pd.to_datetime(start_date)) & 
                 (df['Order Date'] <= pd.to_datetime(end_date)) &
                 (df['Discount'] >= discount_range[0]) 
                 & (df['Discount'] <= discount_range[1])
                 ] 

# Display the filtered dataframe
st.subheader("Filtered Data")
st.write(filtered_df)

