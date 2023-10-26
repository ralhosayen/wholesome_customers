
import streamlit as st
import pandas as pd
import numpy as np
import openai
import os
import csv
import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import altair as alt
from PIL import Image

df = pd.read_csv("wholesome_customers_data.csv")


def main():

    menu = ["Home", "Exploratory Data Analysis", "SQL Playground", "GPT-3.5 Chat", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    conn = sqlite3.connect('database_wholesome_customers_data.db')
    cursor = conn.cursor()

    if choice=="Home":

    	st.markdown("# Wholesome Customers App")
    	image = Image.open('Unknown copy.png')
    	st.image(image)
    	st.write("### App content")
    	st.write ("- This app has 5 sections :")
    	st.write ("1) Home Page")
    	st.write ("2) Exploratory Data Analysis - Data Analysis, Visualization Parts and insights")
    	st.write ("3) SQL Playground - Queries on the original dataset using SQL")
    	st.write ("4) GPT-3.5 Chat Box - Ask your question to Chat-gpt using your API Key")
    	st.write ("5) About - General informations")
    	st.write ("For this project, we are using the wholesome_customers.csv dataset.")
    	st.markdown("---")
    
    elif choice=="Exploratory Data Analysis":

	 st.header('Exploratory Data Analysis')
	st.markdown('## Python for Data Analysis 2')
	st.markdown('#### Wholesome Customers Dataset Analysis') 
	col1, col2, col3 = st.columns(3)
	
	with col1:
		style = "<style>h2 {text-align: center;}</style>"
		st.markdown(style, unsafe_allow_html=True)
		st.subheader("Groceries")
		st.image("https://images.pexels.com/photos/264636/pexels-photo-264636.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")

        with col2:
		style = "<style>h2 {text-align: center;}</style>"
		st.markdown(style, unsafe_allow_html=True)
		st.subheader("Aisles")
		st.image("https://images.pexels.com/photos/4053267/pexels-photo-4053267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
		
	with col3:
		style = "<style>h2 {text-align: center;}</style>"
		st.markdown(style, unsafe_allow_html=True)
		st.subheader("Experiences")
		st.image("https://images.pexels.com/photos/3985060/pexels-photo-3985060.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
		
	st.markdown ('---')
	
	st.header('Exploratory data analysis - (EDA)')
	st.markdown('#### Dataset composition')
	st.markdown('###### The data set has 9 columns with 439 rows')
	
	data=pd.read_csv('wholesome_customers_data.csv')
	st.dataframe(data)
	st.markdown('---')
	df=pd.read_csv('wholesome_customers_data.csv')
	
	region_dist=df['Region'].value_counts()
	channel_dist=df['Channel'].value_counts()
	st.markdown('---')
	st.markdown('###### At regional level, there are 3 main regions were products are sold:')
	    
	with st.container():
		c1,c2=st.columns(2)

	with c1:
		fig,ax=plt.subplots()
		ax.pie(region_dist,autopct='%0.2f%%',labels=['Region 3','Region 1','Region 2'])
		st.pyplot(fig)

	with c2:
		fig,ax=plt.subplots()
		ax.bar(region_dist.index,region_dist)
		st.pyplot(fig)

	with st.expander('Click to see the data'):
		st.dataframe(region_dist)
		
	st.markdown('---')
	st.markdown('###### Regarding channels to purchase, there are 2 main channels identified with the following distribution:')
	    
	with st.container():
		c1,c2=st.columns(2)

	with c1:
		fig,ax=plt.subplots()
		ax.pie(channel_dist,autopct='%0.2f%%',labels=['Channel 1','Channel 2'])
		st.pyplot(fig)

	with c2:
		fig,ax=plt.subplots()
		ax.bar(channel_dist.index,channel_dist)
		st.pyplot(fig)

	with st.expander('Click to see the data'):
		st.dataframe(channel_dist)
		
	st.markdown('---')
	st.markdown('###### We would like to understand better your wholesome buying preferences, please help us to answer the following questions:')
	the_best=st.selectbox('What is your favourite wholesome category?',('Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicassen'))
	st.write('Your selection is:',the_best)
	    
	st.markdown('---')
	    
	regions=st.multiselect('In which regions do you buy your groceries?',['Region 1','Region 2','Region 3'])
	    
	st.markdown('---')
	    
	about_you=st.text_area(label='Talk more about you wholesome preferences')
	    
	your_info=st.button('Submit your data')
	if your_info:
		info={'Favourite wholesome':the_best,'Regions of purchase':regions,'About you':about_you}
		st.json(info)


        
        
     
    elif choice == "SQL Playground": 
         st.markdown("# SQL Playground")

         image = Image.open('Unknown.png')

         st.image(image)

         st.markdown("""
         	## Welcome to Our Database Management Tool

         	This web application is connected to a database, which allows you to manage your data efficiently. Here's how you can get started:

         	**Import Data to Populate the Database (First-Time Use):**
         	- If you're using the application for the first time, you can import data from your computer using a CSV file. This will populate the database with your initial dataset. Please ensure your CSV file is properly formatted.

         	**A Few Important Notes:**
         	- The database can only be populated using the import feature if it is empty. If you have existing data in the database, you'll need to use the next section to perform additional actions such as inserts, updates, or deletes.

         	**Database Management (Existing Data):**
         	- If your database already contains data, you can use the provided tools in the application to manage, update, or delete records as needed. We offer a wide range of features to help you maintain your data.
         	Enjoy using our **Database Management Tool**, and feel free to reach out if you have any questions or need assistance.
         	""")

         cursor.execute("PRAGMA database_list;")
         default_db_path = cursor.fetchall()
         conn.commit()
         conn.close()

         default_db =  os.path.basename(default_db_path[0][2])
         st.info(f"### The default database used in this website is '{default_db}'  --> *status connected*")
         col1,col2 = st.columns(2)

         with col1:
	         uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
	         
	         if uploaded_file is not None:
	            st.write("File Name:", uploaded_file.name)
	            file_name=uploaded_file.name

	         #st.button("Reset", type="primary")
	         if st.button(f"IMPORT FILE TO DATABASE"):
	            df=pd.read_csv(uploaded_file)
	            list_features=df.columns.tolist()
	            table_name = 'table_' + file_name.split('.')[0]
	            db_name = 'database_' + file_name.split('.')[0] + '.db'
	            debug=os.path.exists(db_name)
	            if not os.path.exists(db_name):
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
		            st.write(f"Database '{db_name}' and table '{table_name}' have been created and populated with data from the CSV file.")
		            st.info("The csv file data has been inserted in the database")
	            else:
	            	conn = sqlite3.connect(db_name)
	            	cursor = conn.cursor()

	            	# check if the table is empty
	            	cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
	            	row_count = cursor.fetchone()[0]
	            	if row_count==0:
	            		with open(file_name, 'r') as csv_file:
		            		csv_reader = csv.reader(csv_file)
		            		# Skip the header row
		            		header=next(csv_reader,None)
		            		#Prepare an INSERT INTO statement with placeholders for the columns
		            		placeholders = ', '.join(['?' for _ in header])
		            		insert_sql = f'INSERT INTO {table_name} ({", ".join(header)}) VALUES ({placeholders})'
		            		# Iterate through the rows and insert them into the SQLite database
		            		for row in csv_reader:
		            			cursor.execute(insert_sql, tuple(row))
		            	conn.commit()
		            	st.write(f"Table '{table_name}' in database '{db_name}' has been populated with data from the CSV file.")
		            	st.info("The csv file data has been inserted in the database")
	            	else:
	            		st.warning(f"Table '{table_name}' in database '{db_name}' is not empty. Skipping data insertion.")
	            	conn.close()   
	         # Columns/Layout
         with col2:
         	with st.form(key='query_form'):
         		raw_code = st.text_area("SQL Code Here")
         		submit_code = st.form_submit_button("Execute")
         	# Table of Info
         	with st.expander("Table Info"):
	            """WORKING PROGRESS conn = sqlite3.connect(default_db)
	            cursor = conn.cursor()
	            table_info = f'SELECT COLUMNS FROM {table_name}'
	            cursor.execute(create_table_sql)
	            st.write(table_info)
	            conn.commit()
	            conn.close()"""
         # Results Layouts
         if submit_code:
         	st.info("Query Submitted")
         	st.code(raw_code)
         	# Results
         	query_results = sql_executor(raw_code)
         	with st.expander("Results"):
         		st.write(query_results)
         	with st.expander("Pretty Table"):
         		query_df = pd.DataFrame(query_results)
         		st.dataframe(query_df)   

         st.markdown("---")      



    elif choice == "GPT-3.5 Chat": 

         st.title("GPT-3.5 Turbo Chatbot")

         image = Image.open('Unknown-1.png')

         st.image(image)

         st.markdown("""
         	### This is the integration for Chat-GPT API. 

         	This is how it works :

         	**Import API Key to in a .txt format :**
         	- To use the GPT-3.5, you first need to import your Open AI API Key in a .txt format using the "Browse file" section below.
         	- If the API Key is correctly uploaded, you can see it displaying (masked) below. 

         	**Writing your prompt:**
         	- Write your prompt in the chat box below, press enter and you will see the Chat-GPT answer. """)


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

         st.markdown("---")

        
    elif choice=="About":
        st.write("""## About""")

        st.write("""This app was created by group 5 for the Python II group project.""")
        st.write("Dataset : wholesome_customers.csv")
        st.write("Group members : Camille Delannoy, Julian Gaona, Rawan Alhosayen, Jonathan Garcia.")

        st.markdown("---")

 

main()


