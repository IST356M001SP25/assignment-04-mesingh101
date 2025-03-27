'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx", "json"])

if uploaded_file is not None:
    ext = pl.get_file_extension(uploaded_file.name)
    df = pl.load_file(uploaded_file, ext)
    
    if df is not None:
        st.success("File loaded successfully!")

        all_columns = pl.get_column_names(df)
        selected_columns = st.multiselect("Select columns to display", all_columns, default=all_columns)

        if st.checkbox("Add a filter?"):
            text_columns = pl.get_columns_of_type(df, 'object')

            if text_columns:
                selected_col = st.selectbox("Select a text column to filter", text_columns)
                unique_vals = pl.get_unique_values(df, selected_col)
                selected_val = st.selectbox("Select a value to filter by", unique_vals)

                df_filtered = df[df[selected_col] == selected_val]
            else:
                st.warning("No text columns available for filtering.")
                df_filtered = df
        else:
            df_filtered = df

        df_filtered = df_filtered[selected_columns]

        st.subheader("Filtered Data")
        st.dataframe(df_filtered)

        st.subheader("Descriptive Statistics")
        st.dataframe(df_filtered.describe())
    else:
        st.error("Unsupported file type.")
