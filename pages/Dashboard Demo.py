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

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(
        page_title="Sales Dashboard",
        page_icon=":bar_chart:")

st.markdown(
        """
        This is a prototype dashboard to demonstrate the concept of Streamlit for CDP purposes.
        

        The data is from an open-source.
        
        
        The data used is a sample data from Kaggle.
        """
    )

github_csv_url = 'https://raw.githubusercontent.com/joinnanais/Elemis/main/Sample%20-%20Superstore.csv'
df = pd.read_csv(github_csv_url, encoding='latin1')

st.sidebar.header("Filters")

# Select category filter
category_filter = st.sidebar.multiselect("Select Category", df['Category'].unique(), df['Category'].unique())

# Select sub-category filter
sub_category_filter = st.sidebar.multiselect("Select Sub-Category", df['Sub-Category'].unique(), df['Sub-Category'].unique())

filtered_df = df[(df['Category'].isin(category_filter)) & 
                 (df['Sub-Category'].isin(sub_category_filter))]

# Display the filtered dataframe
st.subheader("Filtered Data")
st.write(filtered_df)





