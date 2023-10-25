import streamlit as st
import pandas as pd
import numpy as np
import os
import csv
import sqlite3 
import openai

df = pd.read_csv("wholesome_customers_data.csv")


def main():

    menu = ["Home", "Exploratory Data Analysis", "SQL Playground", "GPT-3.5 Chat", "Dall-E image Generator", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="Home":

        st.write("### App content")

        st.write ("- This app has XXXX sections :")
        st.write ("1) Home Page")
        st.write ("2) Exploratory Data Analysis - Data Analysis, Visualization Parts and insights")
        st.write ("3) SQL Playground")
        st.write ("4) GPT-4 Chat Box")
        st.write ("5) Dall-E Image Generator")
        st.write ("6) About")


        st.markdown("---")


 
    elif choice=="Exploratory Data Analysis":
        st.write("Exploratory Data Analysis Section")
        
        
     
    elif choice == "SQL Playground": 
         st.write("SQL Playground")

         uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
         
         if uploaded_file is not None:
            st.write("File Name:", uploaded_file.name)
            file_name=uploaded_file.name

         #st.button("Reset", type="primary")
         if st.button('INSERT TO DB'):
            df=pd.read_csv(uploaded_file)
            list_features=df.columns.tolist()
            table_name = 'table_' + file_name.split('.')[0]
            db_name = 'database_' + file_name.split('.')[0] + '.db'
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                # Read the header row to get column names and types
                header = next(csv_reader)
                # Create a table in the database using column names and text data type
                create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join([f"{col} TEXT" for col in header])})'
                cursor.execute(create_table_sql)
                # Prepare an INSERT INTO statement with placeholders for the columns
                placeholders = ', '.join(['?' for _ in header])
                insert_sql = f'INSERT INTO {table_name} ({", ".join(header)}) VALUES ({placeholders})'
                # Iterate through the rows and insert them into the SQLite database
                for row in csv_reader:
                    cursor.execute(insert_sql, tuple(row))

            # Commit the changes and close the database connection
            conn.commit()
            conn.close()
            st.info("The csv file data has been inserted in the database")
            st.dataframe(df)
            st.write(df.columns.tolist())
            st.write(table_name)

         else:
            st.write('NON')

    elif choice == "GPT-3.5 Chat": 

         st.title("GPT-3.5 Turbo Chatbot")

         uploaded_file = st.file_uploader("First, choose a file containing your API Key", type=["txt"])


         if uploaded_file is not None:
            key_bytes = uploaded_file.read()
            key = key_bytes.decode('utf-8').strip()
            masked_key = '*' * (len(key) - 5) + key[-5]
            st.write("API Key:", masked_key)
            openai.api_key = key


         user_input = st.text_input("Then type your prompt below:")


         if user_input:
            response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

            if response['choices'][0]['message']['role'] == 'assistant':
                generated_text = response['choices'][0]['message']['content']
                st.write("Response:")
                st.write(generated_text)

    elif choice == "Dall-E image Generator": 
         st.write("Dall-E image Generator")
        
    elif choice=="About":
        st.write("""

    ## About

    """)

        st.markdown("---")

 

main()


