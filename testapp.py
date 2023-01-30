# Import necessary libraries
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from IPython.display import display, HTML
from PIL import Image

import datetime
import gspread
import hydralit_components as hc
import joblib
import numpy as np
import pandas as pd
import pprint
import qrcode
import random
import re
import requests
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

import streamlit as st
import streamlit.components.v1 as components
import subprocess
import sys
import time
import warnings

# Warnings ignore 
warnings.filterwarnings(action='ignore')
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar options
#option = st.sidebar.selectbox('Navigation', ["Welcome To Fantasty Draft", "How To Play", "Game Setup", The Draft Board", "Community Review", "Player Card"])

#make it look nice from the start
#st.set_page_config(layout='wide',page_title='Fantasy Draft')

#Hide menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
	# specify the primary menu definition
	menu_data = [
	    {'icon': "fa fa-book-open", 'label':"How To Play"},
	    {'icon': "fa fa-chess-board", 'label':"Game Setup"},
	    {'icon': "fa fa-clipboard-list", 'label':"The Draft Board"},
	    {'icon': "fa fa-users", 'label':"Community Review"},
	    {'icon': "fa fa-id-card", 'label':"Player Card"},
	    ]

	over_theme = {'txc_inactive': '#fffae1', 'menu_background':'#0b5c5e',}
	menu_id = hc.nav_bar(
	    menu_definition=menu_data,
	    override_theme=over_theme,
	    home_name='Welcome To Fantasty Draft',
	    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
	    sticky_nav=True, #at the top or not
	    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
	)

	#Welcome To Fantasty Draft
	if menu_id == 'Welcome To Fantasty Draft':

		image = Image.open('fantasy_draft.png')
		st.image(image)

		st.markdown('<div style="text-align: center; fontSize:50px; fontWeight:bold; padding-bottom:30px">Welcome To Fantasty Draft</div>', unsafe_allow_html=True)
		col1,col2, col3, col4= st.columns([1.2,3,.5,.5])
		with col2:
			st.write("Fantasy Draft is a game where players act as the general manager of their own virtual fantasy team. The game consists of drafting and trading picks, setting lineups, and competing against other players' teams to see who comes up on top. The goal of the game is to assemble the best team possible for a given topic. The game is typically played best by those who love to argue for their favorite things.")

	# How To Play
	elif menu_id == "How To Play":
		st.title("How To Play")
		tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Draft Rules","The Basic Draft","The Basic Draft - Snake Draft","Auction Draft","Team Draft","Vote Draft", "Mystery Draft"])
		with tab1:
			st.header("Draft Rules")
			st.subheader("Pick Order")
			st.write("")
			st.markdown("""---""")
			st.subheader("Picking the Prompt")
			st.write("")
			st.markdown("""---""")
			st.subheader("Picks Per Round")
			st.write("")
			st.markdown("""---""")
			st.subheader("Voting")
			st.write("")
			st.markdown("""---""")
			st.subheader("Winning the Game")
			st.write("")
			st.markdown("""---""")
			st.subheader("Variations")
			st.markdown("""
				There are plenty of variations to hold your fantasy draft. Here are some of those:
				- The Basic Draft
				- Snake Draft
				- Auction Draft
				- Team Draft
				- Vote Draft
				- Mystery Draft""")
		with tab2:
			st.header("The Basic Draft")
			col1,col2, col3, col4= st.columns([1,.5,2,.5])
			with col1:
				st.subheader("Game Summary")
			with col3:
				st.subheader("Number of Players: 2 or more")
			st.write("Summary")
			st.subheader("SETUP")
			st.write("")
			st.subheader("PLAY")
			st.write("")
			st.subheader("FAQ")
			st.write("")
			st.subheader("WINNING")
			st.write("")
		with tab3:
			st.header("The Basic Draft - Snake Draft")
			col1,col2, col3, col4= st.columns([1,.5,2,.5])
			with col1:
				st.subheader("Game Summary")
			with col3:
				st.subheader("Number of Players: 2 or more")
			st.write("Summary")
			st.subheader("SETUP")
			st.write("")
			st.subheader("PLAY")
			st.write("")
			st.subheader("FAQ")
			st.write("")
			st.subheader("WINNING")
			st.write("")
		with tab4:
			st.header("Auction Draft")
			col1,col2, col3, col4= st.columns([1,.5,2,.5])
			with col1:
				st.subheader("Game Summary")
			with col3:
				st.subheader("Number of Players: 2 or more")
			st.write("Summary")
			st.subheader("SETUP")
			st.write("")
			st.subheader("PLAY")
			st.write("")
			st.subheader("FAQ")
			st.write("")
			st.subheader("WINNING")
			st.write("")
		with tab5:
			st.header("Team Draft")
			col1,col2, col3, col4= st.columns([1,.5,2,.5])
			with col1:
				st.subheader("Game Summary")
			with col3:
				st.subheader("Number of Players: 2 or more")
			st.write("Summary")
			st.subheader("SETUP")
			st.write("")
			st.subheader("PLAY")
			st.write("")
			st.subheader("FAQ")
			st.write("")
			st.subheader("WINNING")
			st.write("")
		with tab6:
			st.header("Vote Draft")
			col1,col2, col3, col4= st.columns([1,.5,2,.5])
			with col1:
				st.subheader("Game Summary")
			with col3:
				st.subheader("Number of Players: 2 or more")
			st.write("Summary")
			st.subheader("SETUP")
			st.write("")
			st.subheader("PLAY")
			st.write("")
			st.subheader("FAQ")
			st.write("")
			st.subheader("WINNING")
			st.write("")
		with tab7:
			st.header("Mystery Draft")
			col1,col2, col3, col4= st.columns([1,.5,2,.5])
			with col1:
				st.subheader("Game Summary")
			with col3:
				st.subheader("Number of Players: 2 or more")
			st.write("Summary")
			st.subheader("SETUP")
			st.write("")
			st.subheader("PLAY")
			st.write("")
			st.subheader("FAQ")
			st.write("")
			st.subheader("WINNING")
			st.write("")

	# Game Setup
	elif menu_id == "Game Setup":
		st.title("Game Setup")
		col1,col2,col3 = st.columns([1,1,1])
		with col1:
			st.subheader("Players Setup")
			qr_player = Image.open('qr_players.png')
			st.image(qr_player, width=100)

		with col2:
			st.subheader("Draft Order Generator")
			sheet_id = "1zucAAY3FAw9UP5qE3PX9bOP7O3kA5V9qJ4R683bIvGI"
			sheet4_name = "PlayerSetup"
			url4 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet4_name}"
			data4= pd.read_csv(url4, usecols = ["Enter Player's Name"])

			if st.button("Generate Order"):
				random_order=random.sample(list(data4["Enter Player's Name"].unique()), len(data4["Enter Player's Name"].unique()))
				st.markdown('<div style="fontSize:30px; fontWeight:bold">Randomized Order:</div>', unsafe_allow_html=True)
				st.write(*random_order)

		with col3:
			st.subheader("Payment Form")
			qr_image = Image.open('qr_draft.png')
			st.image(qr_image, width=100)

		st.markdown("---")

		# setup the credentials
		#secrets = openai_secret_manager.get_secret("google")
		#scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
		#creds = ServiceAccountCredentials.from_json_keyfile_dict(secrets, scope)
		#client = gspread.authorize(creds)

		sheet_id = "1zucAAY3FAw9UP5qE3PX9bOP7O3kA5V9qJ4R683bIvGI"
		sheet2_name = "AmountLeft"
		url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet2_name}"
		data2= pd.read_csv(url2, usecols = ["Money Per Round"])

		def write_data(enter_money, sheet2_name, row, col):
			sheet = sheet2_name
			sheet.update_cell(row, col, enter_money)

		enter_money = st.text_input("Enter Money Per Round: ")
		if st.button("Enter Money"):
			result = write_data(enter_money, sheet2_name, 2, "G")
			st.success(result)

	# The Draft Board
	elif menu_id == "The Draft Board":
		st.markdown('<div style="text-align: left; fontSize:50px; fontWeight:bold; padding-bottom:30px">The Draft Board</div>', unsafe_allow_html=True)
		col1,col2= st.columns([8,1])
		with col1:
			st.subheader("Players")
			sheet_id = "1zucAAY3FAw9UP5qE3PX9bOP7O3kA5V9qJ4R683bIvGI"
			sheet4_name = "PlayerSetup"
			url4 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet4_name}"
			data4= pd.read_csv(url4, usecols = ["Enter Player's Name"])
			player4 = list(data4["Enter Player's Name"].unique())
			st.write("The players are:", *player4, sep=", ")
		with col2:
			st.subheader("Payment Form")
			qr_image = Image.open('qr_draft.png')
			st.image(qr_image, width=100)
		col1,col2,col3= st.columns([8,0.1,0.1])
		with col1:	
			sheet_id = "1zucAAY3FAw9UP5qE3PX9bOP7O3kA5V9qJ4R683bIvGI"
			sheet5_name = "GeneratedTopic"
			url5 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet5_name}"
			data5= pd.read_csv(url5, usecols = ['Topic'])

			if st.button("Draft Topic"):
				draft_topic=random.sample(list(data5['Topic'].unique()), 1)
				new_draft_topic=''.join(draft_topic)		
				if draft_topic:
					img_path = "./images/" + new_draft_topic + ".png"
					try:
						st.image(img_path, use_column_width=True)
					except:
						st.warning(f"Cannot find an image for the value {new_draft_topic} in the provided path")
		st.markdown("---")		

		sheet_id = "1zucAAY3FAw9UP5qE3PX9bOP7O3kA5V9qJ4R683bIvGI"
		sheet_name = "DraftChoices"
		url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
		data= pd.read_csv(url, usecols = ['Player Name', 'Draft Choice is '])

		col1,col2,col3,col4= st.columns([2,4,.5,1.5])
		with col2:
			gb = GridOptionsBuilder.from_dataframe(data, min_column_width=20)
			gridOptions = gb.build()
			grid_response = AgGrid(
				data,
				gridOptions=gridOptions,
				data_return_mode='AS_INPUT',
				update_mode='MODEL_CHANGED',
				fit_columns_on_grid_load=True,
				theme= 'alpine', #Add theme color to the table
				backgroundColor='#0b5c5e', 
				enable_enterprise_modules=True,
				width='100%',
				reload_data=True,
				)

	# Community Review
	elif menu_id == "Community Review":
		st.markdown('<div style="text-align: left; fontSize:50px; fontWeight:bold; padding-bottom:30px">Community Review</div>', unsafe_allow_html=True)
		
		sheet_id = "1zucAAY3FAw9UP5qE3PX9bOP7O3kA5V9qJ4R683bIvGI"
		sheet_name = "DraftChoices"
		url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
		data= pd.read_csv(url, usecols = ['Player Name', 'Draft Choice is ', 'Paid Price'])
		
		sheet2_name = "Sheet11"
		url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet2_name}"
		data2 = pd.read_csv(url2, usecols = ['Player', 'Amount Left'])

		def search_gsheet(selected_option, search_column, return_column, data2):
			search_result = data2[data2[search_column] == selected_option]
			if not search_result.empty:
				return search_result[return_column].values[0]
			else:
				return "No match found"

		col1,col2, col3, col4= st.columns([2,1,2,1])
		with col1:
			search_cell = st.text_input("Search Draft Board", '')
			if st.button("Search"):
				search = data[(data.apply(lambda row: row.astype(str).str.contains(search_cell, na=False).any(), axis=1))]
				numOfRows = search.shape[0]
				st.write('Results:', numOfRows)
				search
		with col3:
			search_column = 'Player'
			return_column = 'Amount Left'
			selected_option = st.selectbox("Select an option", data2[search_column])
			money_search = search_gsheet(selected_option, search_column, return_column, data2)
			st.write((selected_option +" has "), money_search, (" dollars left"))

		col1,col2,col3,col4= st.columns([8,.5,.5,.5])
		with col1:
			gb = GridOptionsBuilder.from_dataframe(data, min_column_width=30)
			gridOptions = gb.build()
			grid_response = AgGrid(
				data,
				gridOptions=gridOptions,
				data_return_mode='AS_INPUT',
				update_mode='MODEL_CHANGED',
				fit_columns_on_grid_load=True,
				theme= 'alpine', #Add theme color to the table
				backgroundColor='#0b5c5e',
				enable_enterprise_modules=True,
				width='100%',
				reload_data=True,
			)	

	# Player Card
	elif menu_id == "Player Card":
		st.markdown('<div style="text-align: left; fontSize:50px; fontWeight:bold; padding-bottom:30px">Player Card</div>', unsafe_allow_html=True)
		
		sheet_id = "1zucAAY3FAw9UP5qE3PX9bOP7O3kA5V9qJ4R683bIvGI"
		sheet_name = "DraftChoices"
		url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
		data= pd.read_csv(url, usecols = ['Player Name', 'Draft Choice is ', 'Paid Price'])
		sheet2_name = "Sheet11"
		url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet2_name}"
		data2 = pd.read_csv(url2, usecols = ['Player', 'Amount Left'])
		column_name = "Player Name"
		column_name2 = "Player"
		return_column = 'Amount Left'

		def search_gsheet(selected_player_option, column_name2, return_column, data2):
			search_result = data2[data2[column_name2] == selected_player_option]
			if not search_result.empty:
				return search_result[return_column].values[0]
			else:
				return "No match found"
		col1,col2, col3, col4= st.columns([2,1,2,1])
		with col1:
			draft_number = st.selectbox("Enter Number of Draft Picks", [1,2,3,4,5,6,7])
		selected_player_option = st.selectbox("Select an option", data[column_name].unique())
		filtered_player_view = data[data[column_name] == selected_player_option]

		col1 = "Draft Choice is "
		col2 = "Paid Price"

		player_result = filtered_player_view[[col1, col2]]
		money_search = search_gsheet(selected_player_option, column_name2, return_column, data2)

		st.write(player_result)
		st.write((selected_player_option +" has "), money_search, (" dollars left"))

		if selected_player_option:
			draft_count = data[data['Player Name'] == selected_player_option].shape[0]
			new_count = draft_number-draft_count
			if new_count > draft_number:
				st.warning("No more drafts")
			elif new_count <= 0:
				st.success("You have finished drafting")
			else:
				st.write(new_count, "Left to Draft")

if __name__=="__main__":
    main()