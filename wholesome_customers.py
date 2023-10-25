import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("wholesome_customers_data.csv")


def main():

	menu = ["Home", "Exploratory Data Analysis", "SQL Playground", "GPT-4 Chat", "Dall-E image Generator", "About"]

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

	elif choice == "GPT-4 Chat": 
		 st.write("GPT-4 Chat")
		
		 with open('chatgptkey.txt', 'r') as f:
			 api_key = f.read().strip('\n')
			 openai.api_key = api_key

	         
		 def gpt_classify_sentiment(prompt, emotions):
			system_prompt = f'''You are an emotionally intelligent assistant.
                        Classify the sentiment of the user's text with ONLY ONE OF THE FOLLOWING EMOTIONS: {emotions}.
                        After classifying the text, respond with the emotion ONLY.'''
                        response = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': prompt}],max_tokens=20,temperature=0)
                        r = response['choices'][0].message.content
			if r == '':
				r = 'N/A'
			return r

	elif choice == "Dall-E image Generator": 
		 st.write("Dall-E image Generator")
		
	elif choice=="About":
		st.write("""

	## About

	""")

		st.markdown("---")

 

main()


