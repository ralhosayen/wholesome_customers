import streamlit as st
import pandas as pd
import numpy as np
import openai
import os

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

	elif choice == "GPT-3.5 Chat": 
		
		 st.write("GPT-3.5 Turbo Chat")
		 
		 with open('chatgptkey.txt', 'r') as f:
			 api_key = f.read().strip('\n')
                 openai.api_key = api_key
		 
		 user_input = st.text_input("Prompt:")
		 
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


