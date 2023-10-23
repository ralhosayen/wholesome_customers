import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import plotly.graph_objects as go

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
    st.wrrite ("4) GPT-4 Chat Box")
		st.write ("5) Dall-E Image Generator")
    st.write ("6) Dall-E Image Generator")


		st.markdown("---")


 
	elif choice=="Exploratory Data Analysis Section":
		
		
	 
	elif choice == "SQL Playground": 
		 import sqlite3 

        elif choice == "GPT-4 Chat": 
		 st.write("GPT-4 Chat")

        elif choice == "Dall-E image Generator": 
		 st.write("Dall-E image Generator")

	elif choice=="About":
		st.write("""

	## About

	""")

		st.markdown("---")

 

main()


